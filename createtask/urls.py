# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-


#from django.contrib import admin #UsersSiteView, LogginView,
from django.urls import path, include

#app_name = 'index'
from core import views

from django.conf import settings
from django.conf.urls.static import static

from createtask.views import LkTaskView

urlpatterns = [

    path('lk_task/', LkTaskView.as_view(), name='lk_task'),


]



