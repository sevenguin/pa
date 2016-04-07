#-*- coding:utf-8 -*-
from django.conf.urls import url
from . import views

def schedule(request, action):
    return getattr(views, action)(request)

urlpatterns = [
    url(r'^(?P<action>[a-zA-Z]+)/$', schedule, name='jump')
]