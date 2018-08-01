from django.shortcuts import render, HttpResponse
from django.core import serializers
from food.models import *
from django.core.serializers import serialize
import json
from django.http import JsonResponse

def index(request):
    return render(request, 'food/index.html')
   
def user(request):
  return render(request, 'food/user.html')

def testing(request):
  return render(request, 'food/index.html')
  