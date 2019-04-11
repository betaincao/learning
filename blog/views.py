#!/usr/bin/env python
# coding=UTF-8
'''
@Description: In User Settings Edit
@Author: your name
@LastEditors: Please set LastEditors
@Date: 2019-04-10 18:22:03
@LastEditTime: 2019-04-10 19:56:08
'''
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("hello")
def login(request):
    return render(request, 'blog/login/login.html')