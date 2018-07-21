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
      print(request.body)
      return HttpResponse("")
    else:
      return render(request, 'life/home.html')
  
def user(request):
  return render(request, 'life/user.html')
#     if request.method == "POST":
# #       print(json.loads(request.body))
#       return HttpResponse("")
#     else:
# #       all_users = User.objects.all()
# #       response = serialize("json", all_users)
# #       return HttpResponse(response, content_type="application/json")
#       return render(request, 'life/user.html')