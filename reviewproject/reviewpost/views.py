from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import ReviewModel


def signupview(request):
    if request.method == 'POST':
        username = request.POST.get('username_data')
        password = request.POST.get('password_data')
        try:
            user = User.objects.create_user(username, '', password)
            return redirect('login')
        except IntegrityError:
            return render(request, 'signup.html', {'error':'このユーザーは既に登録されています。'})
    else:
        return render(request, 'signup.html', {})

def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username_data')
        password = request.POST.get('password_data')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('list')
        else :
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def listview(request):
    object_list = ReviewModel.objects.all()
    return render(request, 'list.html', {'object_list':object_list})
    
def columnview(request):
    if request.method == 'POST':
        return redirect('login')
    else:
        return render(request, 'login.html', {})
    
def detailview(request, pk):
    object = ReviewModel.objects.get(pk = pk)
    return render(request, 'detail.html', {'object': object})