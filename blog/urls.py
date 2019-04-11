#!/usr/bin/env python
# coding=UTF-8
'''
@Description: In User Settings Edit
@Author: your name
@LastEditors: Please set LastEditors
@Date: 2019-04-10 18:24:29
@LastEditTime: 2019-04-10 18:29:20
'''
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('login/',views.login),
]
