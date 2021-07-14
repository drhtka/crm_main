# -*- coding: utf-8 -*-
from django.urls import path
from lk.views import LkUsersView, LkTaskView, LkAdmin

urlpatterns = [
    path('lk_user/', LkUsersView.as_view(), name='lk_user'),
    path('lk_task/', LkTaskView.as_view(), name='lk_task'),
    path('lk_admin/', LkAdmin.as_view(), name='lk_admin'),


]