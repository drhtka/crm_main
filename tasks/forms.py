# -*- coding: utf-8 -*-
from django import forms
from accounts.models import MyUser

class DateForm(forms.Form):

    time_task = forms.TimeField(input_formats=['%H:%M'],#, '%I:%M %p'
                                widget=forms.TimeInput(attrs={'size': '8',
                                                              'class': 'form-control',
                                                              # 'name': "task_date",
                                                              'placeholder': '12:00',
                                                              'type': 'time'},#form-control
                                                       format=["%H:%M"]), label="", required=True)#, label='Дедлайн', "%I:%M %p"