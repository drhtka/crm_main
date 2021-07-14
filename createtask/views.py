# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import View

from accounts.models import MyUser
from main.models import CreatreTasks


class LkTaskView(LoginRequiredMixin, View):
    # выставлеие задач
    def get(self, request):
        # статус задачи stat_task
        CreatreTasks.objects.filter(id=request.GET.get('task_idd')).update(status_task=request.GET.get('stat_task'))
        # answ_text = Answer.objects.filter(answer_num=request.GET.get('task_idd')).values()
        # print('answ_text')
        # print(answ_text)
        # print_stat =
        # print('print_stat')
        # print(print_stat)
        # print(request.GET.get('task_idd'), request.GET.get('stat_task'))
        return redirect('/lk/')

    # запись в базу поставлененой задачи  id=request.POST.get('id_task'),
    def post(self, request):
        # print(request.POST.get('input_file'))
        # upload file
        print('deline')
        print(request.POST.get('date'))
        myfile = request.FILES['input_file']
        myfile_split = str(myfile).split('.')  # отсекаем все что по точки например .png

        if myfile_split[1] != 'txt':
            return HttpResponse('Формат файла не txt <a href="http://127.0.0.1:8055/lk/">Личный кабинет</a>')
        else:
            # если .txt тогда загрузить
            # print(myfile_split)
            # print(myfile_split[1])
            # .order_by("create_date").last()
            last_id = CreatreTasks.objects.values_list('id').order_by("created").last()
            # print('last_id-2')
            # print(last_id[0])
            last_id_task = CreatreTasks.objects.latest('id').id + 1  # вывели последний айди

            fs = FileSystemStorage()
            filename = fs.save(str(last_id_task) + '.txt', myfile)
            uploaded_file_url = fs.url(filename)
            # print('myfile')
            # print(myfile)
            # print(uploaded_file_url)

            # print(last_id_task.id+1)
            print('role')
            print(request.POST.get('role'))
            id_user = request.POST.get('role')
            idd_user = MyUser.objects.get(pk=id_user)
            username = MyUser.objects.filter(pk=id_user).values('username')
            print('username')
            print(username[0]['username'])
            # print('idd_user')
            # print(request.POST.get('time_task'))
            test_create = CreatreTasks(id_users=idd_user,
                                       inputtitle=request.POST.get('title_task'),
                                       textarea=request.POST.get('desk_task'),
                                       data_dedline=str(request.POST.get('date')),
                                       status_task=1,
                                       time_task=request.POST.get('time_task'),
                                       upload_file_name=str(last_id_task) + '.txt',
                                       username=username[0]['username'],
                                       )
            test_create.save()
            # print('test_create')
            # print(test_create)
            # return HttpResponse('Задача поставлена  <a href="http://127.0.0.1:8005/lk/">Личный кабинет</a>')
            return redirect('/lk_admin/')