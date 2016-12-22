#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('欢迎访问！')
# Create your views here.
