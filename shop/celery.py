# coding:utf-8
from __future__ import absolute_import
from celery import Celery, platforms
from datetime import timedelta
from django.conf import settings
from kombu import Queue, Exchange
import os

platforms.C_FORCE_ROOT = True

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop.settings')

app = Celery('shop')

app.config_from_object('django.conf:settings')
app.conf.update(
    enable_utc=True,
    timezone='Europe/London',
)

app.conf.task_default_queue = 'default'

app.conf.task_queues = (
    Queue('default', exchange=Exchange('default'), routing_key='default'),
    Queue('priority_tasks', exchange=Exchange('priority_tasks'), routing_key='priority_tasks'),
)

app.conf.task_routes = {
    'celery_default_tasks': {
        'queue': 'default',
        'routing_key': 'default'
    },
    'celery_priority_tasks': {
        'exchange': 'processing',
        'exchange_type': 'direct',
        'queue': 'priority_tasks',
        'routing_key': 'priority_tasks'
    }
}

app.conf.update(
    CELERYBEAT_SCHEDULE={
        'sum-task': {
            'task': 'apps.webapp.celery_default_tasks.test',
            'schedule': timedelta(seconds=2),
            'args': ()
        },
    }
)

app.conf.task_default_exchange = 'tasks'
app.conf.task_default_exchange_type = 'topic'
app.conf.task_default_routing_key = 'task.default'


app.autodiscover_tasks([
    'apps.webapp.celery_default_tasks',
    'apps.webapp.celery_priority_tasks'
])

