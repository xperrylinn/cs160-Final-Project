from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('user/', views.user, name='user'),
#     path('searchPage/', views.searchPage, name='searchPage'),
    path('searchHomeQuery/', views.searchHomeQuery, name='searchPageQuery'),
    path('searchUserQuery/', views.searchUserQuery, name='searchPageQuery'),
    path('addReview/', views.addReview, name='addReview')
    # path('activity/',views.activity, name='activity'),
]