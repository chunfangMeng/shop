# coding:utf-8
from __future__ import absolute_import
from celery import Celery, platforms
from datetime import timedelta
from kombu import Queue, Exchange
import os

platforms.C_FORCE_ROOT = True

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop.settings')

app = Celery('shop_celery', backend='redis://127.0.0.1:6379/3', broker='redis://127.0.0.1:6379/3', include=[
    'apps.webapp.celery_default_tasks',
    'apps.webapp.celery_priority_tasks'
])

app.config_from_object('django.conf:settings')
app.conf.update(
    worker_pool_restart=True,
    worker_prefetch_multiplier=1,
    enable_utc=True,
    timezone='Europe/London',
    task_routes={
        'apps.webapp.celery_default_tasks.*': {
            'queue': 'default',
            'routing_key': 'default'
        },
        'apps.webapp.celery_priority_tasks.*': {
            'queue': 'priority_task',
            'routing_key': 'priority_tasks'
        }
    },
    task_queues=(
        Queue('default', exchange=Exchange('default'), routing_key='default'),
        Queue('priority_tasks', exchange=Exchange('priority_tasks'), routing_key='priority_tasks'),
    ),
    CELERYBEAT_SCHEDULE={
        'sum_task': {
            'task': 'apps.webapp.celery_default_tasks.test',
            'schedule': timedelta(seconds=2),
            'args': ()
        },
    }
)

app.conf.task_default_queue = 'default'
app.conf.task_default_exchange = 'tasks'
app.conf.task_default_exchange_type = 'direct'
app.conf.task_default_routing_key = 'default'


app.autodiscover_tasks([
    'apps.webapp.celery_default_tasks',
    'apps.webapp.celery_priority_tasks'
])

