# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from accounts.models import MyUser
from core.forms import ManualForm
from main.models import CreatreTasks
from tasks.forms import DateForm
from datetime import datetime



class LkUsersView(View):
    # личный кабинет пользователя
    def get(self, request, final_array_data=None):

        global id_user_count_name, new_tsk_tmp_array_s, comment, data_comm, comment_s, color_task, no_task, no_task_style
        color_task_data='green'
        from datetime import datetime
        # form = DateForm()
        final_array = []
        if request.GET.get('date'):
            print('расчитываем по выбранной дате')
            print(request.GET.get('date'))

            form_date = DateForm()
            form_manual = ManualForm()
            if request.session.get('my_list') != None:
                user_lk = request.session.get('my_list')
                # print('user_lk')
                # print(user_lk)
                if len(user_lk) == 0:
                    return redirect('accounts:login')
                else:

                    lk_email = MyUser.objects.filter(email=user_lk).values_list('username',
                                                                                'role', 'id')
                # print('lk_email')
                # print(lk_email)
                user_name = lk_email[0][0]
                user_role = lk_email[0][1]
                user_id = lk_email[0][2]
                # print('lk_email')
                # print(user_name, user_role, user_id)
                data_com = []  # чтоб не вызывать ошибок для тех кто входит под номером роли
                comment_s_in_task = []
                layout = ''
                # print('data_user')
                # (request.GET.get('user_id'))
                # print('get')
                # print(request.GET.get('date'))
                data = CreatreTasks.objects.filter(id_users=user_id).filter(
                    data_dedline=request.GET.get('date')).values_list('inputtitle',
                                                                      'textarea',
                                                                      'id_users',
                                                                      'id',
                                                                      'status_task',
                                                                      #'answear',
                                                                      'data_dedline',
                                                                      'time_task',
                                                                      #'answear_comment',
                                                                      'upload_file_name',
                                                                      'slug',
                                                                      'created', )

                # print('hello-131')
                # print(data)
                if len(data) == 0:
                    # print('net zadch-141')
                    no_task = 'По выбранной дате задач нет'
                    no_task_style = 'no_task_style'
                    return render(request, 'lk.html', {'lk_email': user_name,
                                                           'data': data,
                                                       # 'general_arr_task': general_arr_task,
                                                       # 'all_array_end': all_array_end,
                                                           'form_date': form_date,
                                                           'form_manual': form_manual,
                                                           'no_task': no_task,
                                                           'no_task_style': no_task_style,
                                                       })
                else:
                    no_task = 'Задачи по выбранной дате'
                    no_task_style = ''
                    final_array_data = []
                    for all_task_data in data:
                        # print('hello-141')
                        # print('data_dedline')
                        # print(all_task_data[6])
                        tmp_dedline = all_task_data[5].split('-')
                        # print('tmp_dedline')
                        # print(tmp_dedline)
                        year = tmp_dedline[2]
                        month = tmp_dedline[1]
                        day = tmp_dedline[0]
                        deadline = year + '-' + month + '-' + day
                        # print('deadline-1')
                        # print(deadline)
                        # print('hello-4.3')
                        if (month[0] == '0'):
                            month = month[1]

                        if (day[0] == '0'):
                            day = day[1]
                        # print('hello-4.4')
                        # print(year, month, day)

                        # print (now.strftime("%Y-%m-%d %H:%M:%S"))
                        now = datetime.now()
                        now = str(now).split(' ')
                        tod_now = datetime.today()
                        # print('hello-4.now')
                        # print(deadline)
                        deadline = list(deadline)
                        fourty = deadline.pop(4)
                        sexty = deadline.pop(6)
                        deadline = "".join(deadline)

                        now = list(now[0])
                        fourty_n = now.pop(4)
                        sexty = now.pop(6)
                        now = "".join(now)
                        # print('deadline-2')
                        # print(deadline)
                        # print('now')
                        # print(now)
                        # deadline = datetime.strptime('deadline', '%Y%m%d')
                        # print(deadline)
                        # print(type(now[0]))
                        # print('deadline')
                        # color_task = 'green'
                        if int(now) > int(deadline):
                            print("Срок сдачи проекта прошел")
                            color_task_data = 'red'
                        else:
                            period = int(deadline) - int(now)
                            print(period)
                            if period == 0:
                                print("Срок сдачи проекта сегодня")
                                color_task_data = 'blue'
                            else:
                                # print("Осталось {} дней".format(period.days))
                                color_task_data = 'green'
                        tmp_list_data = [all_task_data[0], all_task_data[1], all_task_data[2], all_task_data[3],
                                         all_task_data[4],
                                         all_task_data[5], all_task_data[6], all_task_data[7], all_task_data[8],
                                         all_task_data[9], color_task_data, ]

                        final_array_data.append(tmp_list_data)
                    return render(request, 'lk.html', {'lk_email': user_name,
                                                           'user_role': user_role,
                                                           'data': final_array_data,
                                                       # 'final_array': final_array,
                                                           'form_date': form_date,
                                                           'form_manual': form_manual,
                                                           'no_task': no_task,
                                                           'no_task_style': no_task_style,
                                                       })

        else:
            print('расчитываем по дефолту')
            no_task = 'Задачи'
            no_task_style = ''
            # test_but = request.GET.get('test_but')
            # datepicker = request.GET.get('date')
            # print('test_but')
            # print(test_but, datepicker)
            final_array_data_else = []
            form_date = DateForm()
            form_manual = ManualForm()
            # context = {}
            # context['form'] = DateForm()
            if request.session.get('my_list') != None:
                user_lk = request.session.get('my_list')
                # print('user_lk')
                # print(user_lk)
                if len(user_lk) == 0:
                    return redirect('accounts:login')
                else:

                    lk_email = MyUser.objects.filter(email=user_lk).values_list('username',
                                                                                'role', 'id')
                    # lk_email = MyUser.objects.filter(email=user_lk).exclude(role__in='1').values_list('username',
                    #                                                             'role', 'id')
                # print('lk_email')
                # print(lk_email)
                user_name = lk_email[0][0]
                user_role = lk_email[0][1]
                user_id = lk_email[0][2]
                # print('lk_email')
                # print(user_name, user_role, user_id)
                data_ap = []
                layout = ''
                # print('hello')
                data_data = CreatreTasks.objects.filter(id_users=user_id).values_list('inputtitle',
                                                                                      'textarea',
                                                                                      'id_users',
                                                                                      'id',
                                                                                      'status_task',
                                                                                      #'answear',
                                                                                      'data_dedline',
                                                                                      'time_task',
                                                                                      #'answear_comment',
                                                                                      'upload_file_name',
                                                                                      'slug',
                                                                                      'created', )

                if len(data_data) == 0:
                    # print('net zadch-141')
                    no_task = 'Пока задач нет'
                    no_task_style = 'no_task_style'
                print('data_data')
                # data_ap.append(data)
                print(data_data)
                for data_data_new in data_data:
                    # print('data_data_new')
                    # print(data_data_new)
                    # print(data_data_new[6])
                    tmp_data = data_data_new[5].split('-')
                    # print('tmp_data')
                    # print(tmp_data)
                    year = tmp_data[2]
                    month = tmp_data[1]
                    day = tmp_data[0]
                    all_deline = year + '-' + month + '-' + day
                    # print('all_deline')
                    # print(all_deline)
                    if (month[0] == '0'):# убираем ноль если он есть
                        month = month[1]
                    if (day[0] == '0'):# убираем ноль если он есть
                        day = day[1]
                    # print('111')
                    # print(year, month, day)
                    now = datetime.now()
                    now = str(now).split(' ')
                    all_deline = list(all_deline)
                    fourty = all_deline.pop(4)
                    sexty = all_deline.pop(6)
                    all_deline = "".join(all_deline)

                    now = list(now[0])
                    fourty_n = now.pop(4)
                    sexty = now.pop(6)
                    now = "".join(now)
                    # print('now')
                    # print(now)
                    # print('deadline-1')
                    # print(all_deline)
                    if int(now) > int(all_deline):
                        # print("Срок сдачи проекта прошел")
                        color_task_data = 'red'
                    else:
                        period = int(all_deline) - int(now)
                        # print(period)
                        if period == 0:
                            # print("Срок сдачи проекта сегодня")
                            color_task_data = 'blue'
                        else:
                            # print("Осталось {} дней".format(period.days))
                            color_task_data = 'green'

                    tmp_list_data_else = [data_data_new[0], data_data_new[1], data_data_new[2], data_data_new[3],
                                     data_data_new[4], data_data_new[5], data_data_new[6], data_data_new[7],
                                     data_data_new[8],
                                     data_data_new[9], color_task_data, ]

                    final_array_data_else.append(tmp_list_data_else)
                    # print('final_array_data-1007')
                    # print(final_array_data_else)

                return render(request, 'lk.html', {
                                                       'lk_email': user_name,
                                                       'user_role': user_role,
                                                       'data': final_array_data_else,
                                                       'form_date': form_date,
                                                       'form_manual': form_manual,
                                                       'no_task': no_task,
                                                       'no_task_style': no_task_style,
                                                       })



class LkTaskView(LoginRequiredMixin, View):
    # выставление задачи админом для других пользователей
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
            return HttpResponse('Формат файла не txt <a href="http://127.0.0.1:8005/lk/">Личный кабинет</a>')
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
            # print('role')
            # print(request.POST.get('role'))
            id_user = request.POST.get('role')
            idd_user = MyUser.objects.get(pk=id_user)
            # print('idd_user')
            # print(request.POST.get('time_task'))
            test_create = CreatreTasks(id_users=idd_user,
                                       inputtitle=request.POST.get('title_task'),
                                       textarea=request.POST.get('desk_task'),
                                       data_dedline=str(request.POST.get('date')),
                                       status_task=1,
                                       time_task=request.POST.get('time_task'),
                                       upload_file_name=str(last_id_task) + '.txt')
            test_create.save()
            # print('test_create')
            # print(test_create)
            # return HttpResponse('Задача поставлена  <a href="http://127.0.0.1:8005/lk/">Личный кабинет</a>')
            return redirect('/lk_user/')

class LkAdmin(LoginRequiredMixin, View):
    # Админка
    # выводим все задачи или фильтруем по дате
    def get(self, request):
        from datetime import datetime
        if request.GET.get('date'):
            print('расчитываем по выбранной дате')
            no_task = 'задачи по выбранной дате'
            no_task_style = ''
            print(request.GET.get('date'))
            form_date = DateForm()
            form_manual = ManualForm()
            all_task = ''  # инициализировали переменную для избежния ошибок, чтоб не было конфликтов
            all_task = CreatreTasks.objects.filter(data_dedline__iexact=request.GET.get('date')) \
                .values_list('id',
                             'id_users',
                             'inputtitle',
                             'textarea',
                             'created',
                             #'answear',
                             'status_task',
                             #'answear_comment',
                             'data_dedline',
                             'time_task',
                             'upload_file_name',
                             )
            final_array = []
            # print('hello-4')
            # print(all_task)
            # i = 0
            if len(all_task) == 0:
                # print('net zadch-141')
                no_task = 'По выбранной дате задач нет'
                no_task_style = 'no_task_style'
                task_list_users = MyUser.objects.all()  # .values_list('username', 'id')
                # выбираем для подсчета времени затраченную на задачу
                users_distinct_task = CreatreTasks.objects.filter(status_task=2).values('id_users').order_by(
                    'id_users').distinct('id_users')
                # print('hello-8')
                # print('users_distinct_task')
                # print(users_distinct_task)
                # sum_time_users = []
                # sum_time_users2 = []
                all_array = []
                for users_distinct_task_s in users_distinct_task:
                    u_distr = users_distinct_task_s['id_users']  # номера пользователей которые выполнили задачи
                    user_time_task = CreatreTasks.objects.filter(status_task=2).filter(
                        id_users=u_distr).values_list(
                        'time_task')  # все часы котрые потратил польз на выполнение задачи
                    time_task_us = 0
                    arr_time_user = []
                    tmp_time = 0
                    tmp_username = ''
                    print('user_time_task-1334')
                    print(user_time_task)
                    for user_time_task_s in user_time_task:
                        time_task_us = str(u_distr) + ',' + user_time_task_s[0]

                        id_user_count = time_task_us.split(',')[0]
                        # print('hello-9')
                        # print(time_task_us)
                        time_task_all = time_task_us.split(',')[1]
                        id_user_count = MyUser.objects.filter(id=id_user_count).values('username')
                        # print('hello-10')
                        # print('id_user_count')
                        # print(id_user_count)
                        id_user_count_name = id_user_count[0]['username']
                        tmp_object = [id_user_count_name, time_task_all]
                        arr_time_user.append(tmp_object)
                        # print('hello-11')
                        # print('tmp_username')
                        # print(tmp_username)
                        time_task_all = time_task_all.split(':')
                        # print('hello-12')
                        time_task_h = time_task_all[0]
                        # print('hello-13')
                        # print(time_task_all)
                        time_task_m = int(time_task_all[1]) / 60
                        # print('hello-14')
                        time_task_all_all = int(time_task_h) + time_task_m
                        # print('hello-15')
                        # print('time_task_all_all')
                        # print(time_task_all_all)
                        # sum_time_users = [id_user_count_name, (time_task_all_all)]
                        # print('sum_time_users ')
                        # print(sum_time_users )
                    my_sum = ''
                    # tmp_ar2 = []
                    tmp_ar3 = [id_user_count_name, '']
                    # print('tmp_ar3')
                    # print(tmp_ar3)
                    for arr_time_user_s in arr_time_user:
                        my_sum = my_sum + ',' + arr_time_user_s[1]
                        tmp_ar3[1] = my_sum
                    # print('tmp_ar3')
                    # print(tmp_ar3)
                    all_array.append(tmp_ar3)
                # print('all_array')
                # print(all_array)
                all_array_end = []
                for all_array_s in all_array:
                    split_time = all_array_s[1].split(',')
                    hours = 0
                    minuts = 0
                    our_time = 0
                    all_array_time = [all_array_s[0], '', '']
                    # print('hello-16')
                    # print(split_time)
                    for split_time_s in split_time:
                        if split_time_s != '':  # 36 min 28 urok
                            split_two = split_time_s.split(':')
                            hours = int(hours) + int(split_two[0])
                            minuts = int(minuts) + round(int(split_two[1]) / 60)
                            our_time = hours + minuts
                            all_array_time[1] = our_time
                            zp_user = MyUser.objects.filter(username=all_array_time[0]).values_list('zp')

                            all_zp = our_time * int(zp_user[0][0])
                            all_array_time[2] = all_zp
                    all_array_end.append(all_array_time)
                return render(request, 'lk_admin.html', {
                                                       # 'general_arr_task': general_arr_task,
                                                       'all_array_end': all_array_end,
                                                        'final_array': all_task,
                                                       'form_date': form_date,
                                                       'form_manual': form_manual,
                                                       'no_task': no_task,
                                                       'no_task_style': no_task_style,
                                                       })
            else:
                no_task = 'Задачи по выбранной дате'
                no_task_style = ''
                final_array_data = []
                for all_task_s in all_task:
                    # print('hello-4.2')
                    # print('data_dedline')
                    # print(all_task_s[8])
                    tmp_dedline = all_task_s[8].split('-')
                    # print('tmp_dedline')
                    # print(tmp_dedline)
                    year = tmp_dedline[2]
                    month = tmp_dedline[1]
                    day = tmp_dedline[0]
                    deadline = year + '-' + month + '-' + day
                    # print('deadline-1')
                    # print(deadline)
                    # print('hello-4.3')
                    if (month[0] == '0'):
                        month = month[1]

                    if (day[0] == '0'):
                        day = day[1]
                    # print('hello-4.4')
                    # print(year, month, day)

                    # print (now.strftime("%Y-%m-%d %H:%M:%S"))
                    now = datetime.now()
                    now = str(now).split(' ')
                    # tod_now = datetime.today()
                    # print('hello-4.now')
                    # print(deadline)
                    deadline = list(deadline)
                    fourty = deadline.pop(4)
                    sexty = deadline.pop(6)
                    deadline = "".join(deadline)

                    now = list(now[0])
                    fourty_n = now.pop(4)
                    sexty = now.pop(6)
                    now = "".join(now)
                    # print('deadline-2')
                    # print(deadline)
                    # print('now')
                    # print(now)
                    # deadline = datetime.strptime('deadline', '%Y%m%d')
                    # print(deadline)
                    # print(type(now[0]))
                    # print('deadline')
                    # color_task = 'green'
                    if int(now) > int(deadline):
                        # print("Срок сдачи проекта прошел")
                        color_task = 'red'
                    else:
                        period = int(deadline) - int(now)
                        # print(period)
                        if period == 0:
                            # print("Срок сдачи проекта сегодня")
                            color_task = 'blue'
                        else:
                            # print("Осталось {} дней".format(period.days))
                            color_task = 'green'
                    # print('all_task_s[9]')
                    # print(all_task_s[9])
                    # print('hello-5')
                    user_id_name = MyUser.objects.filter(id=all_task_s[1]).values(
                        'username')  # приравнивем айди к пользователю
                    username_lk = user_id_name[0]['username']
                    # print(general_arr_task[i])
                    # print('general_arr_task')
                    tmp_list = [all_task_s[0], all_task_s[1], all_task_s[2], all_task_s[3], all_task_s[4],
                                all_task_s[5],
                                all_task_s[6], all_task_s[7], username_lk, all_task_s[8], color_task,
]  # здесь соединяем две таблицы
                    final_array.append(tmp_list)
                    #     print('hello-6')
                    #     #i = i + 1
                    print('final_array-1285')
                    print(final_array)

                    task_list_users = MyUser.objects.all()  # .values_list('username', 'id')
                    # выбираем для подсчета времени затраченную на задачу
                    users_distinct_task = CreatreTasks.objects.filter(status_task=2).values('id_users').order_by(
                        'id_users').distinct('id_users')
                    # print('hello-8')
                    # print('users_distinct_task')
                    # print(users_distinct_task)
                    # sum_time_users = []
                    # sum_time_users2 = []
                    all_array = []
                    for users_distinct_task_s in users_distinct_task:
                        u_distr = users_distinct_task_s['id_users']  # номера пользователей которые выполнили задачи
                        user_time_task = CreatreTasks.objects.filter(status_task=2).filter(
                            id_users=u_distr).values_list(
                            'time_task')  # все часы котрые потратил польз на выполнение задачи
                        time_task_us = 0
                        arr_time_user = []
                        tmp_time = 0
                        tmp_username = ''
                        print('user_time_task-1334')
                        print(user_time_task)
                        for user_time_task_s in user_time_task:
                            time_task_us = str(u_distr) + ',' + user_time_task_s[0]

                            id_user_count = time_task_us.split(',')[0]
                            # print('hello-9')
                            # print(time_task_us)
                            time_task_all = time_task_us.split(',')[1]
                            id_user_count = MyUser.objects.filter(id=id_user_count).values('username')
                            # print('hello-10')
                            # print('id_user_count')
                            # print(id_user_count)
                            id_user_count_name = id_user_count[0]['username']
                            tmp_object = [id_user_count_name, time_task_all]
                            arr_time_user.append(tmp_object)
                            # print('hello-11')
                            # print('tmp_username')
                            # print(tmp_username)
                            time_task_all = time_task_all.split(':')
                            # print('hello-12')
                            time_task_h = time_task_all[0]
                            # print('hello-13')
                            # print(time_task_all)
                            time_task_m = int(time_task_all[1]) / 60
                            # print('hello-14')
                            time_task_all_all = int(time_task_h) + time_task_m
                            # print('hello-15')
                            # print('time_task_all_all')
                            # print(time_task_all_all)
                            # sum_time_users = [id_user_count_name, (time_task_all_all)]
                            # print('sum_time_users ')
                            # print(sum_time_users )
                        my_sum = ''
                        # tmp_ar2 = []
                        tmp_ar3 = [id_user_count_name, '']
                        # print('tmp_ar3')
                        # print(tmp_ar3)
                        for arr_time_user_s in arr_time_user:
                            my_sum = my_sum + ',' + arr_time_user_s[1]
                            tmp_ar3[1] = my_sum
                        # print('tmp_ar3')
                        # print(tmp_ar3)
                        all_array.append(tmp_ar3)
                    # print('all_array')
                    # print(all_array)
                    all_array_end = []
                    for all_array_s in all_array:
                        split_time = all_array_s[1].split(',')
                        hours = 0
                        minuts = 0
                        our_time = 0
                        all_array_time = [all_array_s[0], '', '']
                        # print('hello-16')
                        # print(split_time)
                        for split_time_s in split_time:
                            if split_time_s != '':  # 36 min 28 urok
                                split_two = split_time_s.split(':')
                                hours = int(hours) + int(split_two[0])
                                minuts = int(minuts) + round(int(split_two[1]) / 60)
                                our_time = hours + minuts
                                all_array_time[1] = our_time
                                zp_user = MyUser.objects.filter(username=all_array_time[0]).values_list('zp')

                                all_zp = our_time * int(zp_user[0][0])
                                all_array_time[2] = all_zp
                        all_array_end.append(all_array_time)
                        # print('hello-17')
                        # print('all_array_end')
                        # print(all_array_end)
                    # context = {}
                    # context['form'] = DateForm()
                    # print('form_date')
                    # print(form_date)
                    return render(request, 'lk_admin.html', {
                                                           # 'lk_email': user_name,
                                                           # 'user_role': user_role,
                                                           'task_list_users': task_list_users,
                                                           'all_task': all_task,
                                                           'final_array': final_array,
                                                           # 'general_arr_task': general_arr_task,
                                                           'all_array_end': all_array_end,
                                                           'form_date': form_date,
                                                           'form_manual': form_manual,
                                                           'no_task': no_task,
                                                           'no_task_style': no_task_style,
                                                           # 'form_date_create': form_date_create
                                                           })
        else:
            print('расчитываем по дефолту')
            no_task = 'Задачи '
            no_task_style = ''
            form_date = DateForm()
            form_manual = ManualForm()
            all_task = ''  # инициализировали переменную для избежния ошибок, чтоб не было конфликтов
            all_task = CreatreTasks.objects.filter() \
                                            .values_list('id',
                                                         'id_users',
                                                         'inputtitle',
                                                         'textarea',
                                                         'created',
                                                         #'answear',
                                                         'status_task',
                                                         #'answear_comment',
                                                         'data_dedline',
                                                         'time_task',
                                                         'upload_file_name',
                                                         )
            final_array = []
            # print('hello-4')
            # print(all_task)
            # i = 0
            for all_task_s in all_task:
                # print('hello-4.2')
                # print('data_dedline')
                # print(all_task_s[8])
                tmp_dedline = all_task_s[6].split('-')
                # print('tmp_dedline')
                # print(tmp_dedline)
                year = tmp_dedline[2]
                month = tmp_dedline[1]
                day = tmp_dedline[0]
                deadline = year + '-' + month + '-' + day
                # print('deadline-1')
                # print(deadline)
                # print('hello-4.3')
                if (month[0] == '0'):
                    month = month[1]

                if (day[0] == '0'):
                    day = day[1]
                # print('hello-4.4')
                # print(year, month, day)

                # print (now.strftime("%Y-%m-%d %H:%M:%S"))
                now = datetime.now()
                now = str(now).split(' ')
                # tod_now = datetime.today()
                # print('hello-4.now')
                # print(deadline)
                deadline = list(deadline)
                fourty = deadline.pop(4)
                sexty = deadline.pop(6)
                deadline = "".join(deadline)

                now = list(now[0])
                fourty_n = now.pop(4)
                sexty = now.pop(6)
                now = "".join(now)
                # print('deadline-2')
                # print(deadline)
                # print('now')
                # print(now)
                # deadline = datetime.strptime('deadline', '%Y%m%d')
                # print(deadline)
                # print(type(now[0]))
                # print('deadline')
                # color_task = 'green'
                if int(now) > int(deadline):
                    # print("Срок сдачи проекта прошел")
                    color_task = 'red'
                else:
                    period = int(deadline) - int(now)
                    # print(period)
                    if period == 0:
                        # print("Срок сдачи проекта сегодня")
                        color_task = 'blue'
                    else:
                        # print("Осталось {} дней".format(period.days))
                        color_task = 'green'
                # print('all_task_s[9]')
                # print(all_task_s[9])
                # print('hello-5')
                user_id_name = MyUser.objects.filter(id=all_task_s[1]).values(
                    'username')  # приравнивем айди к пользователю
                username_lk = user_id_name[0]['username']
                # print(general_arr_task[i])
                # print('general_arr_task')
                tmp_list = [all_task_s[0], all_task_s[1], all_task_s[2], all_task_s[3], all_task_s[4],
                            all_task_s[5],
                            all_task_s[6], all_task_s[7], username_lk, all_task_s[8], color_task,
                            ]  # здесь соединяем две таблицы
                final_array.append(tmp_list)
                #     print('hello-6')
                #     #i = i + 1
                # print('final_array-1518')
                # print(final_array)
                #     new_tsk_tmp_array = final_array[0][7].split(',')
                #     print(new_tsk_tmp_array)
                #     for new_tsk_tmp_array_s in new_tsk_tmp_array:
                #         print('new_tsk_tmp_array_s')
                #         print(new_tsk_tmp_array_s)
                # print('hello-7')
                # print('user_role')
                # print(user_role)
                # my_loyout = ''
                # if int(user_role) == 1:
                #     # print('админ')
                #     my_loyout = 'main/lk_admin.html'
                # if int(user_role) == 2:
                #     # print('Бухгалтер')
                #     my_loyout = 'main/lk.html'
                # if int(user_role) == 3:
                #     # print('Менеджер')
                #     my_loyout = 'main/lk_manager.html'
                # if int(user_role) == 4:
                #     # print('Оператор интернет')
                #     my_loyout = 'main/lk_oper_inet.html'
                # if int(user_role) == 5:
                #     # print(data)
                #     # print('Оператор ктв')
                #     my_loyout = 'main/lk_oper_ktv.html'
                # print('hello-7.1')
                # выбираем имя и id  для передачи в шаблон и создания задачи динамически
                task_list_users = MyUser.objects.all()  # .values_list('username', 'id')
                # выбираем для подсчета времени затраченную на задачу
                users_distinct_task = CreatreTasks.objects.filter(status_task=2).values('id_users').order_by(
                    'id_users').distinct('id_users')
                # print('hello-8')
                # print('users_distinct_task')
                # print(users_distinct_task)
                # sum_time_users = []
                # sum_time_users2 = []
                all_array = []
                for users_distinct_task_s in users_distinct_task:
                    u_distr = users_distinct_task_s['id_users']  # номера пользователей которые выполнили задачи
                    user_time_task = CreatreTasks.objects.filter(status_task=2).filter(
                        id_users=u_distr).values_list(
                        'time_task')  # все часы котрые потратил польз на выполнение задачи
                    time_task_us = 0
                    arr_time_user = []
                    tmp_time = 0
                    tmp_username = ''
                    # print('user_time_task-1566')
                    # print(user_time_task)
                    for user_time_task_s in user_time_task:
                        time_task_us = str(u_distr) + ',' + user_time_task_s[0]

                        id_user_count = time_task_us.split(',')[0]
                        # print('hello-9')
                        # print(time_task_us)
                        time_task_all = time_task_us.split(',')[1]
                        id_user_count = MyUser.objects.filter(id=id_user_count).values('username')
                        # print('hello-10')
                        # print('id_user_count')
                        # print(id_user_count)
                        id_user_count_name = id_user_count[0]['username']
                        tmp_object = [id_user_count_name, time_task_all]
                        arr_time_user.append(tmp_object)
                        # print('hello-11')
                        # print('tmp_username')
                        # print(tmp_username)
                        time_task_all = time_task_all.split(':')
                        # print('hello-12')
                        time_task_h = time_task_all[0]
                        # print('hello-13')
                        # print(time_task_all)
                        time_task_m = int(time_task_all[1]) / 60
                        # print('hello-14')
                        time_task_all_all = int(time_task_h) + time_task_m
                        # print('hello-15')
                        # print('time_task_all_all')
                        # print(time_task_all_all)
                        # sum_time_users = [id_user_count_name, (time_task_all_all)]
                        # print('sum_time_users ')
                        # print(sum_time_users )
                    my_sum = ''
                    # tmp_ar2 = []
                    tmp_ar3 = [id_user_count_name, '']
                    # print('tmp_ar3')
                    # print(tmp_ar3)
                    for arr_time_user_s in arr_time_user:
                        my_sum = my_sum + ',' + arr_time_user_s[1]
                        tmp_ar3[1] = my_sum
                    # print('tmp_ar3')
                    # print(tmp_ar3)
                    all_array.append(tmp_ar3)
                # print('all_array')
                # print(all_array)
                all_array_end = []
                for all_array_s in all_array:
                    split_time = all_array_s[1].split(',')
                    hours = 0
                    minuts = 0
                    our_time = 0
                    all_array_time = [all_array_s[0], '', '']
                    # print('hello-16')
                    # print(split_time)
                    for split_time_s in split_time:
                        if split_time_s != '':  # 36 min 28 urok
                            split_two = split_time_s.split(':')
                            hours = int(hours) + int(split_two[0])
                            minuts = int(minuts) + round(int(split_two[1]) / 60)
                            our_time = hours + minuts
                            all_array_time[1] = our_time
                            zp_user = MyUser.objects.filter(username=all_array_time[0]).values_list('zp')

                            all_zp = our_time * int(zp_user[0][0])
                            all_array_time[2] = all_zp
                    all_array_end.append(all_array_time)
                    # print('hello-17')
                    # print('all_array_end')
                    # print(all_array_end)
                # context = {}
                # context['form'] = DateForm()
                # print('form_date')
                # print(form_date)
            return render(request, 'lk_admin.html', {
                # 'lk_email': user_name,
                # 'user_role': user_role,
                'task_list_users': task_list_users,
                'all_task': all_task,
                'final_array': final_array,
                # 'general_arr_task': general_arr_task,
                'all_array_end': all_array_end,
                'form_date': form_date,
                'form_manual': form_manual,
                'no_task': no_task,
                'no_task_style': no_task_style,
                # 'form_date_create': form_date_create
            })