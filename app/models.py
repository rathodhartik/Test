
from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError



def validate_capitalized(value):
        if value != value.capitalize():
            raise ValidationError('Invalid (not capitalized) value: %(value)s',params={'value': value})
        
    

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100,validators=[validate_capitalized])
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