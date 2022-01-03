
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    address=models.TextField()
    age=models.IntegerField()
  

    

    def __str__(self):
        return self.name
    
    
class Profile(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='profile')
    
    
    def __str__(self):
        return self.firstname