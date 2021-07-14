# -*- coding: utf-8 -*-
from django.contrib import admin
from main.models import CreatreTasks


class CreateTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'inputtitle', 'created', 'data_dedline', 'id_users', 'username')
    list_filter = ('id', 'created', 'username')
    list_display_links = ['id', 'inputtitle']
    list_editable = ['data_dedline', 'data_dedline']
    prepopulated_fields = {'slug': ('inputtitle',)}
    list_per_page = 20
    # fields = ('data_dedline')


admin.site.register(CreatreTasks, CreateTaskAdmin)
