# -*- coding: utf-8 -*-
from datetime import date, datetime, timedelta, timezone
from django.utils.timezone import now
from django.utils import datetime_safe, formats
# from datetime import datetime, timedelta
# datetime.date()
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.db.models import SET_NULL
from django.utils.formats import get_format
from main.utils import from_cyrillic_to_eng
from accounts.models import MyUser, Roles


class CreatreTasks(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, null=False)
    id_users = models.ForeignKey(MyUser, verbose_name='Почта', null=True, blank=False, on_delete=SET_NULL)#, to_field='id'
    # id_userss = models.ForeignKey(MyUser, null=True, blank=False, on_delete=SET_NULL, db_column="username")#, to_field='id'
    # id_users = models.IntegerField(blank=True, null=True)
    inputtitle = models.CharField('Название',max_length=50, blank=True, null=True, unique=True,)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    textarea = models.TextField('Текст',max_length=300, blank=True, null=True)
    created = models.DateField('Дата создания', auto_now_add=False, default=date.today, blank=True,)
    # created = models.DateField('Дата создания', auto_now_add=False, default=date.today, blank=True, datetime.now().strftime('%d.%m.%Y'))
    data_dedline = models.CharField('Дата work', blank=True, null=True, max_length=300,)
    # answear = models.TextField('Комментарии', blank=True)

    working = '1'
    and_task = '2'
    cancel = '3'
    not_executed = '4'

    SELECT_STATUS = (
        (working, 'В работе'),
        (and_task, 'Закончена'),
        (cancel, 'Отменена'),
        (not_executed, 'Не выполнена'),
    )
    status_task = models.CharField('Статус задачи', max_length=15, choices=SELECT_STATUS, blank=False, default=1)

    # status_task = models.PositiveIntegerField(blank=True, null=True)
    # answear_comment = models.TextField('Ответ', blank=True)
    time_task = models.TimeField('Время выполнения', max_length=4, blank=True, default='12:00')
    upload_file_name = models.CharField('Файл', blank=True, max_length=255)
    username = models.CharField('Имя', blank=True, max_length=255)
    # username = models.ForeignKey(MyUser, null=True, blank=False, on_delete=SET_NULL)

    # administrator = '1'
    # buhgalter = '2'
    # menager = '3'
    # operator_inet = '4'
    # operator_ktv = '5'
    # SELECT_ROLE = (
    #     (administrator, 'Администратор'),
    #     (buhgalter, 'Бухгалтер'),
    #     (menager, 'Менеджер'),
    #     (operator_inet, 'Оператор интернет'),
    #     (operator_ktv, 'Оператор ктв'),
    # )
    role = models.ForeignKey(Roles, null=True, blank=True, on_delete=SET_NULL, default=3)

    # tags = GenericRelation(MyUser)
    class Meta:
        #managed = True
        ordering = ('-id',)
        db_table = 'createtask'
        verbose_name = 'Задачи'
        verbose_name_plural = 'Задачи'
    def __str__(self):
        return self.inputtitle

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.inputtitle))
        super().save(*args, **kwargs)

