# -*- coding: utf-8 -*-


#from django.contrib import admin #UsersSiteView, LogginView,
from django.urls import path
from tasks.views import TasskCardView
#app_name = 'index'


urlpatterns = [

    path('taskcard', TasskCardView.as_view(), name='taskcard'),

]
