from django.db import models


class UploadImage(models.Model):
    hash_key = models.CharField(max_length=64, null=True, blank=True, help_text='md5 key')
    url_path = models.CharField(max_length=128, null=True, blank=True, help_text='图片地址')
    image = models.TextField(null=True, blank=True, help_text='图片base64')

    class Meta:
        db_table = 'upload_image'
