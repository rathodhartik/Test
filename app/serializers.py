from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from .models import City, Country, Student ,Profile
from app import models
from django.core.exceptions import ValidationError



# StudentSerializer
class StudentSerializer(serializers.Serializer):
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


# CountrySerializer
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
      model = Country
      fields = '__all__'
      
      def create(self,validate_data):
         return Country.objects.create(**validate_data)
      def update(self, instance, validated_data):
         instance.name=validated_data.get('name',instance.name)
         instance.save()
         return instance
   
# CitySerializer
class CitySerializer(serializers.ModelSerializer):
   class Meta:
      model = City
      fields = '__all__'
      
   def create(self, validated_data):
      country = Country.objects.get(name=validated_data['country'])
      validated_data['country'] = country
      city_instance = City.objects.create(**validated_data)
      print(city_instance)
      return city_instance
   
   # def validate(self,data):
   #    name = data['name']
   #    city =City.objects.filter(name__iexact=name)
   #    if city.exists():
   #       raise ValidationError("taken name")   
   
      



# UserSerializer
class UserSerializer(serializers.ModelSerializer):
   class Meta:
      model = User
      fields = ['username','email']
      
      

# ProfileSerializer
class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    country =CountrySerializer()
    city = CitySerializer()
   
    class Meta:
      model = Profile
      fields="__all__"
      
      
    def create(self,validate_data):
      return Profile.objects.create(**validate_data)






   
   




