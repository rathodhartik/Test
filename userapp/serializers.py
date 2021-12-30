from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
   class Meta:
      model = Profile
      fields = "__all__"
      
      
class UserSerializer(serializers.ModelSerializer):
   pro = ProfileSerializer()
   class Meta:
      model = User
      fields = "__all__"
