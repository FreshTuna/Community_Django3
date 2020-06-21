from django.urls import path, include
from .import views

urlpatterns= [
    path('', views.main),
    path('login/', views.send_to_login, name="send_to_login"),
    path('board/', views.send_to_board, name="send_to_board"),
    path('register/', views.send_to_register, name="send_to_register"),
]
