from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

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
            print('ログイン成功です!!!')
        else :
            print('Userが存在しません')
        return render(request, 'login.html', {})
    else:
        return render(request, 'login.html', {})