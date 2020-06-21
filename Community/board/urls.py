from django.urls import path, include
from . import views

urlpatterns=[
    path('detail/<int:pk>', views.board_detail),
    path('list/', views.board_list),
    path('write/',views.board_write),
]