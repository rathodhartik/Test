from rest_framework import serializers

from django.contrib.auth.models import User

from userapp.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
   class Meta:
      model = Profile
      fields = "__all__"
      

class UserSerializer(serializers.ModelSerializer):
   pro=ProfileSerializer(read_only=True)
   
   class Meta:
      model = User
      fields = ['username','email','pro']


      
