# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from accounts.models import MyUser, Roles
from comments.models import Comments
from main.models import CreatreTasks
from tasks.forms import DateForm





class TasskCardView(LoginRequiredMixin, View):
    # Подробно о задаче
    # ловим айдишник задачи и выводим все данные о ней
    def get(self, request):
        global final_array, comment
        form_date = DateForm()
        id_task = CreatreTasks.objects.filter(id=request.GET.get('task')).values('id', 'id_users', 'inputtitle',
                                                                                 'textarea', 'created',
                                                                                 'status_task',
                                                                                 'time_task', 'role', 'slug',
                                                                                 'upload_file_name',
                                                                                 'data_dedline',
                                                                                 'username',)

        print('id_task')
        print(id_task)
        user_id_name = MyUser.objects.filter(id=id_task[0]['id_users']).values('username', 'role')
        user_task_name = user_id_name[0]['username']
        user_id_roles = Roles.objects.filter(id_roles=user_id_name[0]['role']).values('roles')
        user_task_roles = user_id_roles[0]['roles']
        # print('user_id_roles')
        # print(user_id_roles)
        # id_coment = CreatreTasks.objects.filter().values('id')
        #
        # for id_coment_s in id_coment:
        #     print('id_coment')
        #     print(id_coment_s['id'])
        comment = Comments.objects.filter(answer_num=id_task[0]['id']).values()
        # print('comment')
        # print(comment)

        return render(request, 'taskcard.html', {"final_array": id_task,
                                                 'user_task_name': user_task_name,
                                                 'user_task_roles': user_task_roles,
                                                 'comment': comment,
                                                 'form_date': form_date})  # 'id_task': id_task, 'final_array': final_array

    def post(self, request):
        # print(request.POST.get('id_state_task'), request.POST.get('stat_task'))
        # print('id_state_task')
        CreatreTasks.objects.filter(id=request.POST.get('id_state_task')).update(
            status_task=request.POST.get('stat_task'))
        referer = self.request.META.get('HTTP_REFERER')
        return redirect(referer)
