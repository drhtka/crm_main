# -*- coding: utf-8 -*-
from django.contrib import admin
from comments.models import Comments


# Register your models here.
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('date_answer', 'answer_num', 'owner_id')
    # ist_display_links = ('date_answer', 'owner_id')
    list_filter = ('answer_num', 'date_answer')
    # list_editable = ['answer_num', 'date_answer']


admin.site.register(Comments, CommentsAdmin)
