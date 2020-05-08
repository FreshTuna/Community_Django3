from django.shortcuts import render, redirect
from .models import User
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password
from .forms import LoginForm

# Create your views here.

def home(request):
    user_id = request.session.get('user')
    if user_id:
        user=User.objects.get(pk=user_id)
        return HttpResponse(user.username)

    return HttpResponse("Home!")

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')

def login(request):
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')

    else:
        form = LoginForm
    return render(request, 'user/login.html',{'form':form})



def register(request):
    if request.method =="GET":
        return render(request, 'user/register.html')
    elif request.method =='POST':
        username =request.POST.get('username',None)
        password = request.POST.get('password',None)
        re_password = request.POST.get('re-password',None)
        useremail = request.POST.get('useremail',None)

        res_data ={}

        if not (username and password and re_password):
            res_data['error']
        elif password != re_password:
            res_data['error'] = "비밀번호가 다릅니다."
        else:
            user = User(
                username=username,
                useremail=useremail,
                password=make_password(password)
            )
            user.save()

        return render(request,'user/register.html',res_data)

