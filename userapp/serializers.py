from rest_framework import serializers

from django.contrib.auth.models import User

# from userapp.models import Profile



class UserSerializer(serializers.ModelSerializer):
   class Meta:
      model = User
      fields = ['id','username','email']


# class ProfileSerializer(serializers.Serializer):
#    class Meta:
#       model = Profile
#       fields = "__all__"
      
      
