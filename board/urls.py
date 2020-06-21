from django.urls import path, include
from . import views

urlpatterns=[
    path('detail/<int:pk>', views.board_detail, name="board_detail"),
    path('list/', views.board_list, name="board_list"),
    path('write/',views.board_write, name="board_write"),
    path('sendhome/',views.send_to_home, name="send_to_home")
]