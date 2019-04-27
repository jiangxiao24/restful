#!user/bin/env python
# -*- coding:utf-8 -*-
#__author__:jiangqijun
#__date__:2019/3/20

from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path(r'index/', views.index),
    #path('snippets/', views.snippet_list),
    #path('snippets/<int:pk>/', views.snippet_detail),
    path('snippets/', views.Snippets_list.as_view()),
    #path('snippets/<int:pk>/', views.Snippet_detail.as_view()),
    # path('snippets/', views.SnippetList.as_view()),
    # path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    # path('users/', views.UserList.as_view()),
    # path('users/<int:pk>/', views.UserDetail.as_view()),
    # path(r'^$', views.api_root),
    # path(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view()),
]

# urlpatterns = format_suffix_patterns([
#     path(r'index/', views.index),
#     path('', views.api_root),
#     path('snippets/',
#         views.SnippetList.as_view(),
#         name='snippet-list'),
#     path('snippets/<int:pk>/',
#         views.SnippetDetail.as_view(),
#         name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/',
#         views.SnippetHighlight.as_view(),
#         name='snippet-highlight'),
#     path('users/',
#         views.UserList.as_view(),
#         name='user-list'),
#     path('users/<int:pk>/',
#         views.UserDetail.as_view(),
#         name='user-detail')
# ])

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from snippets import views
#
# router = DefaultRouter()
# router.register(r'snippets', views.SnippetViewSet)
# router.register(r'users', views.UserViewSet )
# urlpatterns = [
#     path('', include(router.urls)),
#     path(r'test/', views.test)
# ]