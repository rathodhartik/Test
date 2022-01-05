
from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError



def validate_capitalized(value):
        if value != value.capitalize():
            raise ValidationError('Invalid (not capitalized) value: %(value)s',params={'value': value})
        

def only_char(value): 
    if value.isalpha()==False:
        raise ValidationError('int value not access')
    
def validate_age(value):
        if 0< value <= 100:
            return value
        raise ValidationError('Age not valid')      

class Student(models.Model):
    name=models.CharField(max_length=100,validators=[validate_capitalized])
    address=models.TextField()
    age=models.IntegerField(validators=[validate_age])

    def __str__(self):
        return self.name 


class Country(models.Model):
    country= models.CharField(max_length=20)
    
    def __str__(self):
        return self.country
    
class State(models.Model):
    state=models.CharField(max_length=20)
    country = models.ForeignKey(Country,on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.state
    
class City(models.Model):
    city=models.CharField(max_length=20)
    state=models.ForeignKey(State,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.city
    
    
    
class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    
    
    firstname=models.CharField(max_length=100,validators=[only_char])
    lastname=models.CharField(max_length=100,validators=[only_char])
    age=models.IntegerField(validators=[validate_age])
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    city=models.ForeignKey(Country,on_delete=models.CASCADE,null=True,blank=True)
    state=models.ForeignKey(State,on_delete=models.CASCADE,null=True,blank=True)
    country=models.ForeignKey(City,on_delete=models.CASCADE,null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='profile')
    
    def __str__(self):
        return self.firstname
    
