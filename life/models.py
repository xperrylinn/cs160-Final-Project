from django.db import models

class Group(models.Model):
	established = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=50)
  
class User(models.Model):
  username = models.CharField(max_length=30, primary_key=True)
  password = models.CharField(max_length=50)
  name = models.CharField(max_length=100)
  age = models.IntegerField(null = True)
  hometown = models.CharField(max_length=30)
  
  def __str__(self):
    return self.username
    
class Home(models.Model):
  address = models.CharField(max_length=50, primary_key=True)
  price = models.IntegerField()
  landlord = models.CharField(max_length=30)
  
  def __str__(self):
    return self.address