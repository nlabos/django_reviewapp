# reviewpost/views.py

from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import ReviewModel

from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


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

@login_required
def listview(request):
    object_list = ReviewModel.objects.all()
    return render(request, 'list.html', {'object_list':object_list})

@login_required
def columnview(request):
    if request.method == 'POST':
        return redirect('login')
    else:
        return render(request, 'login.html', {})
    
@login_required
def detailview(request, pk):
    object = ReviewModel.objects.get(pk = pk)
    return render(request, 'detail.html', {'object': object})

@login_required
def evaluationview(request, pk):
    post = ReviewModel.objects.get(pk=pk)
    post.useful_num = post.useful_num + 1
    post.save()
    return redirect('list')

def logoutview(request):
    logout(request)
    return redirect('login')

class CreateClass(CreateView):
    template_name = 'create.html'
    model = ReviewModel
    fields = ('author', 'title', 'content', 'product_image')
    success_url = reverse_lazy('list')