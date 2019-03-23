#!user/bin/env python
# -*- coding:utf-8 -*-
#__author__:jiangqijun
#__date__:2019/3/22


from __future__ import absolute_import, unicode_literals
import os
from celery import Celery, platforms

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restful.settings')
app = Celery('restful')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
platforms.C_FORCE_ROOT = True

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


from celery.schedules import crontab
from datetime import timedelta

app.conf.update(
    CELERYBEAT_SCHEDULE = {
        'sum-task': {
            'task': 'deploy.tasks.add',
            'schedule':  timedelta(seconds=20),
            'args': (5, 6)
        },
        'send-report': {
            'task': 'deploy.tasks.report',
            'schedule': crontab(hour=4, minute=30, day_of_week=1),
        }
    }
)