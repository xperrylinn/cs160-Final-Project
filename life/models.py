from django.db import models

class Group(models.Model):
	established = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=50)
  
class User(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    photo = models.CharField(max_length=500)
    hometown = models.CharField(max_length=30)
    # many to many object of revies
    # search
    
    
class Home(models.Model):
  address = models.CharField(max_length=50, primary_key=True)
  price = models.

    
    
# Username
# String
# Password
# String
# Name
# String 
# Photo
# String
# Hometown
# String 
# Reviews
# Array of strings to User Review Models
# Search
# String 
