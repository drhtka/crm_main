# -*- coding: utf-8 -*-
import datetime

from django.db import models

# Create your models here.
from django.utils.datetime_safe import date


class Comments(models.Model):
    answer_num = models.CharField('Номер задачи', max_length=30, blank=True)

    date_answer = models.DateTimeField('Дата создания', auto_now_add=True, blank=True, )
    owner_name = models.CharField('Имя пользователя', max_length=30, blank=True)
    owner_id = models.CharField('ID пользователя', max_length=3, blank=True)
    slug_task_com = models.CharField('slug', max_length=255, blank=True)
    answer_text = models.TextField('Комментарий', blank=True)

    class Meta:
        # managed = True
        db_table = 'comments'
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.answer_num