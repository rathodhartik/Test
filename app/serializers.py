from rest_framework import serializers
from .models import Student

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