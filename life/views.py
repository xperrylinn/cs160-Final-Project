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
    
def review(request):
    if request.method == "POST":
      newReviewData = json.loads(request.body.decode('ASCII'))
      query_address = newReviewData['address']
      print(query_address)
      # Check if address is valid 
      exists = Home.objects.filter(address=query_address).exists()
      print(exists)
      if exists:
        query_home = Home.objects.get(address=query_address)
        Review(home=query_home, rating=int(newReviewData['rating']), review=newReviewData['review']).save()
        return HttpResponse("")
      else:
        return HttpResponse(status=400)
    else:
      return render(request, 'life/review.html')

  
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
    
def helper(review):
    data = {
      'success': 'true',
      'address': review.home.address,
      'rating': review.rating,
      'review': review.review
    }
    return data

def searchHomeReviewQuery(request):
    query_address = request.GET.get('address', None)
    home_exists = Home.objects.filter(address=query_address).exists()
    if home_exists:
      query_home = Home.objects.get(address=query_address)
      review_exists = Review.objects.filter(home=query_home).exists()
      if review_exists:
        reviews = Review.objects.filter(home=query_home)
        obj = {}
        counter = 0
        for review in reviews:
          obj["review" + str(counter)] = helper(review)
          counter = counter + 1
        return JsonResponse(obj)
      else:
        # Review doesn't exist
        data = {
          'success': 'review_error'
        }
        return JsonResponse(data)
    else:
      # Home doesn't exist
      data = {
        'success': 'home_error'
      }
      return JsonResponse(data)    

  

  
  
  
  
  