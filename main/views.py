from django.shortcuts import render,redirect

# Create your views here.

def main(request):
    return render(request, 'main/main.html')

def send_to_login(request):

    return redirect('/user/login')

def send_to_board(request):

    return redirect('/board/list')

def send_to_register(request):

    return redirect('/user/register')