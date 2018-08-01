from django.db import models
 
class User(models.Model):
  username = models.CharField(max_length=30, primary_key=True)
  password = models.CharField(max_length=50)
  name = models.CharField(max_length=100)
  
  def __str__(self):
    return self.username

class Testing(models.Model):
  test = models.CharField(max_length=30, primary_key=True)
  test2 = models.CharField(max_length=30)
    