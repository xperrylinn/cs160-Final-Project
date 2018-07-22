from django.shortcuts import render, HttpResponse
from django.core import serializers
from life.models import *
from django.core.serializers import serialize
import json
from django.http import JsonResponse

def index(request):
    all_homes = Home.objects.all()
    all_users = User.objects.all()
    return render(request, 'life/index.html', {"homes": all_homes, "users": all_users})
  
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
    
def searchPage(request):
    return render(request, 'life/searchPage.html')

  
def searchHomeQuery(request):
    query_address = request.GET.get('address', None)
    exists = Home.objects.filter(address=query_address).exists()
    if exists:
      home = Home.objects.get(address=query_address)
      data = {
        'success': 'true',
        'address': home.address,
        'price': home.price,
        'landlord': home.landlord
      }
      return JsonResponse(data)
    else:
      data = {
        'success': 'false'
      }
      return JsonResponse(data)

def searchUserQuery(request):
    query_name = request.GET.get('name', None)
    exists = User.objects.filter(name=query_name).exists()
    if exists:
      user = User.objects.get(name=query_name)
      data = {
        'success': 'true',
        'username': user.username,
        'name': user.name,
        'age': user.age,
        'hometown': user.hometown
      }
      return JsonResponse(data)
    else:
      data = {
        'success': 'false'
      }
      return JsonResponse(data)