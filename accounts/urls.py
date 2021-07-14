# -*- coding: utf-8 -*-
from django.urls import path
from accounts.views import (
    login_view, logout_view, register_view, RolesView,#, update_view, delete_view, contact
)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('roles/', RolesView.as_view(), name='roles'),
    # path('update/', update_view, name='update'),
    # path('delete/', delete_view, name='delete'),
    # path('contact/', contact, name='contact'),
]
