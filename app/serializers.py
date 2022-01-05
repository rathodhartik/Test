from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from .models import Country, State, Student ,Profile
from app import models




class StudentSerializer(serializers.Serializer):
   # class Meta:
   #    model = Student
   #    fields = "__all__"
   #id=serializers.IntegerField() 
   name=serializers.CharField(max_length=100)
   address=serializers.CharField(max_length=100)
   age=serializers.IntegerField()

   # Create
   def create(self,validate_data):
      return Student.objects.create(**validate_data)
   
   # Update
   def update(self, instance, validated_data):
      instance.name=validated_data.get('name',instance.name)
      instance.address=validated_data.get('address',instance.address)
      instance.age=validated_data.get('age',instance.age)
      instance.save()
      return instance


class CountrySerializer(serializers.Serializer):
   country=serializers.CharField(max_length=20)
      
   def create(self,validate_data):
      return Country.objects.create(**validate_data)
   
   def update(self, instance, validated_data):
      instance.country=validated_data.get('country',instance.country)
      instance.save()
      return instance
   
   

class StateSerializer(serializers.Serializer):
   state=serializers.CharField(max_length=20)
   country=serializers.CharField(max_length=20)
      
   def create(self,validate_data):
      return State.objects.create(**validate_data)
   
   def update(self, instance, validated_data):
      instance.state=validated_data.get('state',instance.state)
      instance.country=validated_data.get('country',instance.country)
      return instance




class UserSerializer(serializers.ModelSerializer):
   class Meta:
      model = User
      fields = ['username','email']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
      model = Profile
      fields = ['firstname','lastname','user']






   
   




