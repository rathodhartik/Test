from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    age=models.IntegerField(default=0)
    address=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='profile')
    
    
    def __str__(self):
        return self.firstname