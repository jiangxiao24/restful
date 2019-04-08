#!user/bin/env python
# -*- coding:utf-8 -*-
#__author__:jiangqijun
#__date__:2019/4/3

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from usermanage import views


# router = DefaultRouter()
# router.register(r'snippets', views.SnippetViewSet)
# router.register(r'users', views.UserViewSet )
urlpatterns = [
    path(r'login/', views.login),
    path(r'index/', views.index),
    path(r'nocookie/', views.nocookie),
    path(r'operate_session/', views.operate_session),
    path(r'login_view/', views.login_view),
    path(r'handle_classes/', views.handle_classes),
]