from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('user/', views.user, name='user'),
    # path('activity/',views.activity, name='activity'),
]