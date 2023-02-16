import redis
import time

from django.conf import settings


class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


class DistributedLock(metaclass=Singleton):
    def __init__(self, cache_key, cache_type, time_out=20):
        self.client = self.__get_redis_client__()
        self.cache_key = cache_key
        self.cache_type = cache_type
        self.time_out = time_out

    @classmethod
    def __get_redis_client__(cls):
        pool = redis.ConnectionPool(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)
        return redis.StrictRedis(connection_pool=pool)

    def get_write_lock(self, value):
        val = value + ':' + self.cache_type
        while True:
            res = self.client.set(self.cache_key, val, nx=True, ex=self.time_out)
            if res:
                # 表示获得锁成功，跳出循环
                break
            else:
                # 此时说明已经存在数据
                # 表示等待锁的过程，但是有一种情况是：如果检测到锁为读锁，来的操作也是读操作，那么不阻塞
                if self.cache_type == 'read':
                    check_type = str(self.redis_con.get(self.cache_key).decode()).split(':')[1]
                    if check_type == 'read':
                        break
            time.sleep(0.1)

    def del_lock(self, val):
        val = val + ':' + self.cache_type
        old_val = self.client.get(self.cache_key)
        if old_val == val.encode():
            self.redis_con.delete(self.cache_key)