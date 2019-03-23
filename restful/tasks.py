#!user/bin/env python
# -*- coding:utf-8 -*-
#__author__:jiangqijun
#__date__:2019/3/22

from __future__ import absolute_import
from celery import shared_task


@shared_task
def add(x, y):
    print('##############')
    return x + y
