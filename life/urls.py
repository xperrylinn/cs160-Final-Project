from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('user/', views.user, name='user'),
    path('searchHomeQuery/', views.searchHomeQuery, name='searchPageQuery'),
    path('searchUserQuery/', views.searchUserQuery, name='searchPageQuery'),
    path('searchHomeReviewQuery/', views.searchHomeReviewQuery, name='searchPageQuery'),
    path('review/', views.review, name='review')
]