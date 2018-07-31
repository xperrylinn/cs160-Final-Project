from django.shortcuts import render, HttpResponse
from django.core import serializers
from food.models import *
from django.core.serializers import serialize
import json
from django.http import JsonResponse

def index(request):
    all_homes = Home.objects.all()
    all_users = User.objects.all()
    return render(request, 'food/index.html', {"homes": all_homes, "users": all_users})
   
def user(request):
  return render(request, 'food/user.html')
  