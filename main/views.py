# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.
from accounts.models import MyUser
from main.models import CreatreTasks


class MainPageView(View):
    # page registration
    def get(self, request):
        # for user in Users.objects.all():
        #     # user.set_password(user.password)
        #     # print(user.password)
        #     user.save()
        print(request.session.get('my_list'))
        if request.session.get('my_list') != None:
            # request.session['my_list'] = []
            print('1')
        else:
            print('2')
            request.session['my_list'] = []
            print('em')
            print(request.session['my_list'])
        user_time_task = CreatreTasks.objects.all()
        user_id_name_zp = MyUser.objects.filter()
        return render(request, 'main.html',
                      {'final_array': user_time_task, 'user_id_name_zp': user_id_name_zp[0:5]})