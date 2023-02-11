from celery import task
import time


@task
def test():
    print('>>>>>>>')
    time.sleep(2)
    print('end>>>>')
    return ''
