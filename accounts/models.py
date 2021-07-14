# -*- coding: utf-8 -*-
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils.html import format_html

class MyUserManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=self.get_by_natural_key(username)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            username,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):

    class Meta:
        verbose_name = 'Аккаунты'
        verbose_name_plural = 'Аккаунты'
    #user_email
    username = models.CharField('Имя', max_length=255, blank=False, null=False, unique=True, default='NewUser')
    email = models.CharField('Почта', max_length=100, blank=True, null=True, unique=True,)# было user_email
    password = models.CharField('Пароль', max_length=255, blank=True, null=True)

    administrator = '1'
    buhgalter = '2'
    menager = '3'
    operator_inet = '4'
    operator_ktv = '5'

    SELECT_ROLE = (
        (administrator, 'Администратор'),
        (buhgalter, 'Бухгалтер'),
        (menager, 'Менеджер'),
        (operator_inet, 'Оператор интернет'),
        (operator_ktv, 'Оператор ктв'),
    )

    role = models.CharField('Должность', max_length=15, choices=SELECT_ROLE, blank=False, default=3)
    zp = models.CharField('Зарплата', max_length=100, blank=True)
    is_active = models.BooleanField('Активный', default=True)
    is_admin = models.BooleanField('Доступ', default=False)
    send_email = models.BooleanField(default=True, verbose_name='Почта')

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def colored_name(self):
        return format_html(
            '<span style="color: #ff0FFF;">{} {}</span>',
            self.username,
            self.pk,
        )

    def __int__(self):
        return self.username
        # return "Логин: {} id: {}".format(self.username, self.pk)

class Roles(models.Model):
    id_roles = models.AutoField(primary_key=True, auto_created=True)
    roles = models.CharField(max_length=30, blank=True)

    administrator = '1'
    buhgalter = '2'
    menager = '3'
    operator_inet = '4'
    operator_ktv = '5'
    SELECT_ROLE = (
        (administrator, 'Администратор'),
        (buhgalter, 'Бухгалтер'),
        (menager, 'Менеджер'),
        (operator_inet, 'Оператор интернет'),
        (operator_ktv, 'Оператор ктв'),
    )
    role = models.CharField('Должность', max_length=15, choices=SELECT_ROLE, blank=False, default=3)

    class Meta:
        #managed = True
        verbose_name = 'Должность'
        verbose_name_plural = 'Должность'


    def __str__(self):
        return self.roles