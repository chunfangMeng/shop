from django.db import models


class DownloadManageTask(models.Model):
    DownloadStatus = (
        ('PENDING', 0),
        ('SUCCESS', 1),
        ('ACTIVE', 2),
        ('FAILED', 3),
        ('RETRIED', 4),
    )
    download_key = models.CharField(max_length=36, unique=True, db_index=True, help_text='下载id')
    status = models.IntegerField(default=0, help_text='状态', choices=DownloadStatus)
    runtime = models.FloatField(default=0, help_text='运行时间')
    local_file = models.TextField(null=True, help_text='本地文件')
    cloud_file = models.CharField(max_length=128, null=True, blank=True, help_text='云文件地址')
    create_at = models.DateTimeField(auto_now_add=True, help_text='创建日期')
    last_update = models.DateTimeField(auto_now=True, help_text='最新一次更新')
    operator = models.CharField(max_length=150, help_text='操作人用户名')

    class Meta:
        db_table = 'download_manage_task'

    def __str__(self):
        return f'{self.download_key} - {self.status}'
