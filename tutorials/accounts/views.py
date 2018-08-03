# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from accounts.forms import RegistrationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from accounts.forms import EditProfile
from django.contrib.auth.decorators import login_required


def firstpage(request):
    return render(request,'accounts/firstpage.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return redirect('/accounts/register/')
        return redirect('/accounts/login/')
    else :
        form = RegistrationForm()
        arg ={'form' : form }
        return render(request,'accounts/reg_form.html',arg)

@login_required
def profile(request):
    args = {'user':request.user}
    return render(request , 'accounts/profile.html',args)

@login_required
def editprofile (request):
    if request.method == 'POST':

        form = EditProfile(request.POST,instance = request.user)

        if form.is_valid():
            form.save()
            return redirect('/accounts/profile/')
    else :
        form = EditProfile(instance = request.user)
        args={'form': form}
        return render(request,'accounts/edit_profile.html',args)

@login_required
def changepassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST,user = request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request , form.user)
            return redirect('/accounts/profile/')
        else :
            return redirect('/accounts/changepassword/')

    else :
        form = PasswordChangeForm(user = request.user)
        args={'form': form}
        return render(request,'accounts/change_password.html',args)
