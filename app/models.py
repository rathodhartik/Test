from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    address=models.TextField()
    age=models.IntegerField()
    marks=models.IntegerField()#added by rishi

    

    def __str__(self):
        return self.name