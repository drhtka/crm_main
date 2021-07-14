# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView

from .models import Comments
# Create your views here.
from main.models import CreatreTasks #Users,
# class CommetnsView(ListView):
#
#
#     def get(self, request):
#         global comment
#         id_coment = CreatreTasks.objects.filter().values('id')
#
#         for id_coment_s in id_coment:
#             print('id_coment')
#             print(id_coment_s['id'])
#             comment = Comments.objects.filter(answer_num=id_coment_s['id']).values()
#             print('comment')
#             print(comment)
#         return render(request, 'main/taskcard.html', {'comment': comment})

#
# class CommentView(LoginRequiredMixin, View):
#     # изменение часов дедлайна
#     def post(self, request):
#         # print('mayak')
#         # print(request.POST.get('comment'))
#         # print(request.POST.get('user_id'))
#         # print(request.POST.get('task_id'))
#         time_task = request.POST.get('time_task')
#         print('post_time')
#         print(time_task)
#         # filter_coment = CreatreTasks.objects.filter(id=request.POST.get('task_id')).values('answear')
#         # print('filter_coment')
#         # temp_com = (filter_coment[0]['answear'])
#         # temp_com = temp_com + ',' + request.POST.get('comment') + '<br>'
#         # print(temp_com)
#         com_create = CreatreTasks.objects.filter(id=request.POST.get('task_id')) \
#             .update(time_task=time_task)
#         print('com_create')
#         print(com_create)
#         # com_create.save()
#         # return redirect('/lk/')
#         referer = self.request.META.get('HTTP_REFERER')  # вернуться на предыдущую страницу на тот жу урл
#         return redirect(referer)

class CommentCreateViews(View):
    # отправка комента в базу
    def post(self, request):
        print('1')
        print(request.POST.get('comm_user_id'))
        # print('2')
        # print(request.POST.get('comment'))
        # print('3')
        # print(request.POST.get('id_com_task'))
        # print('4')
        # print(str(request.POST.get('id_com_task')))
        coment_create = Comments(answer_num=request.POST.get('id_com_task'),
                                 owner_name=request.POST.get('comm_user'),
                                 owner_id=request.POST.get('comm_user_id'),
                                 slug_task_com=request.POST.get('slug-com_task'),
                                 answer_text=request.POST.get('comment'),
                                 )

        coment_create.save()
        referer = self.request.META.get('HTTP_REFERER')
        return redirect(referer)




    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['comment'] = Comments.objects.all()[:5]
    #     print('comment')
    #     print(context)
    #     return context
