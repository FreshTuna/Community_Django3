from django.shortcuts import render, redirect
from .models import Board
from user.models import User
from django.core.paginator import Paginator
from .form import BoardForm

def board_write(request):
    if request.method=='POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            user = User.objects.get(pk=user_id)

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = user
            board.save()

            return redirect('/board/list')

    else:
        form = BoardForm()
    return render(request,'board/board_write.html',{'form':form})

def board_list(request):
    boards = Board.objects.all().order_by('-id')
    paginator = Paginator(boards,6)
    page = request.GET.get('page')
    pages = paginator.get_page(page)
    page_range = list(paginator.page_range[0:len(paginator.page_range)])

    return render(request,'board/board_list.html',{'boards':boards, 'pages':pages, 'page_range':page_range})
# Create your views here.


def board_detail(request, pk):
    board = Board.objects.get(pk=pk)

    return render(request, 'board/board_detail.html', {'board':board})

def send_to_home(request):
    return redirect('/')
