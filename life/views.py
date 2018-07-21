from django.shortcuts import render, HttpResponse
from django.core import serializers
from life.models import *
from django.core.serializers import serialize
import json

def index(request):
    all_homes = Home.objects.all()
    all_users = User.objects.all()
    return render(request, 'life/index.html', {"homes": all_homes, "users": al})
  
def home(request):
    if request.method == "POST":
      newHomeData = json.loads(request.body.decode('ASCII')) # Decode bystring to string and convert to ditionary
      Home(address=newHomeData['address'], price=int(newHomeData['price']), landlord=newHomeData['landlord']).save()
      return HttpResponse("")
    else:
      return render(request, 'life/home.html') 
   
def user(request):
    if request.method == "POST":
      newUserData = json.loads(request.body.decode('ASCII'))
      User(newUserData['username'], newUserData['password'], newUserData['name'], int(newUserData['age']), newUserData['hometown']).save()
      return HttpResponse("")
    else:
      return render(request, 'life/user.html')