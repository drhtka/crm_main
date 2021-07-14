# -*- coding: utf-8 -*-
from django.urls import path, include
from main.views import MainPageView

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    ]