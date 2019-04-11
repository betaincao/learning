#!/usr/bin/env python
# coding=UTF-8
'''
@Description: In User Settings Edit
@Author: your name
@LastEditors: Please set LastEditors
@Date: 2019-04-10 18:21:30
@LastEditTime: 2019-04-10 18:28:06
'''
"""learning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]
