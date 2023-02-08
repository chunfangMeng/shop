# coding:utf-8
from __future__ import absolute_import
from celery import Celery, platforms
from kombu import Queue
import os

platforms.C_FORCE_ROOT = True

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop.settings')

app = Celery('shop')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.update(
    enable_utc=True,
    timezone='Europe/London',
)

app.conf.task_default_queue = 'default'

app.conf.task_routes = {
    'apps.webapp.celery_default_tasks': {
        'queue': 'default'
    },
    'apps.webapp.celery_priority_tasks': {
        'queue': 'priority_tasks'
    }
}

app.conf.task_default_exchange = 'tasks'
app.conf.task_default_exchange_type = 'topic'
app.conf.task_default_routing_key = 'task.default'

app.conf.task_queues = (
    Queue('default', routing_key='default'),
    Queue('priority_tasks', routing_key='priority_tasks'),
)

app.autodiscover_tasks([
    'apps.webapp.celery_default_tasks',
    'apps.webapp.celery_priority_tasks'
])

