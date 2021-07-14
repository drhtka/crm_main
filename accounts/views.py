# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout, get_user_model
from django.views import View

from accounts.forms import UserLoginForm, UserRegistrationForm
from django.contrib import messages
# Create your views here.
from accounts.models import Roles, MyUser

User = get_user_model()

def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        email = data.get('email')
        password = data.get('password')
        user = authenticate(request, email=email, password=password)
        print('user')
        print(user)
        login(request, user)
        request.session['my_list'] = email
        print('em')
        print(request.session['my_list'])

        return redirect('/')
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')

def register_view(request):
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()
        print('new_user')
        print(new_user)
        # messages.success(request, 'Пользователь добавлен в систему.')
        return render(request, 'accounts/register_done.html',
                      {'new_user': new_user})
    return render(request, 'accounts/register.html', {'form': form})

class RolesView(LoginRequiredMixin, View):
    # смена ролей на шаблоне из выпадающего списка
    def get(self, request):
        roles_edit_list = []
        roles_edit_listt = []
        list_tmp = []
        roles_edit = MyUser.objects.all().values_list('username', 'email', 'id', 'role', 'role')
        # print('roles_edit')
        # print(roles_edit)
        for roles_edit_s in roles_edit:
            roles_edit_list.append(roles_edit_s)
            # print('roles_edit')
            # print(roles_edit_list)
            for roles_edit_s_s in roles_edit_list:
                p = Roles(role=roles_edit_s[3])
                role_name = p.get_role_display()
                list_tmp = list(roles_edit_s_s)
                list_tmp[4] = role_name
            # print('role_name')
            # print(list_tmp)
            roles_edit_listt.append(list_tmp)
        # print('roles_edit_listt')
        # print(roles_edit_listt)
        rolis_list = Roles.objects.all().values()  # values_list('id_roles', 'roles')
        # print('rolis_list')
        # print(rolis_list)
        return render(request, 'roles.html', {'roles_edit': roles_edit,
                                               'rolis_list': rolis_list,
                                               'role_name': roles_edit_listt})

    def post(self, request):
        # print('user_hidddd')
        # print(request.POST.get('rolless'))
        id_up = request.POST.get('rolless')
        # print('user_hid')
        # print(request.POST.get('user_hid'))
        email_up = request.POST.get('user_hid')
        # print('user_hid-2')
        update_user = MyUser.objects.filter(email=email_up).update(role=id_up)
        # print(update_user)
        return redirect('/accounts/roles/')