
from functools import partial
from django.shortcuts import render


from app.utilities import *

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from django.http import Http404
from django.http import HttpResponse,JsonResponse
import io
from copy import error

from django.contrib.auth.models import User
from .models import Profile,Student,Country,State,City


from .serializers import CountrySerializer, ProfileSerializer, StateSerializer, StudentSerializer, UserSerializer


from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view



# Template use
@login_required(login_url='login_view')
def base1(request):
    return render(request,"app/base1.html")

@login_required(login_url='login_view')
def home(request):
     return render(request,'app/home.html')
 
def homepage(request):
    return render(request,'app/homepage.html')





#CRUD API
class student_list(APIView):
    #permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(success_added("Data successfully inserted",serializer.data),status=CREATED)
        return Response(data_fail("Data Invalid",serializer.errors),status=BAD_REQUEST)


class student_detail(APIView):
    #permission_classes = [permissions.IsAuthenticated]
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk ):
        stu = self.get_object(pk)
        serializer = StudentSerializer(stu)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        stu = self.get_object(pk)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(update_data("Data successfully updated",serializer.data),status=OK)
        return Response(data_fail("Update Invalid",serializer.errors),status=BAD_REQUEST)
    
    def patch(self, request, pk):
        stu = self.get_object(pk)
        serializer = StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(update_data("Data Successfully Updated",serializer.data),status=OK)
        return Response(data_fail("Update Invalid",serializer.errors),status=BAD_REQUEST)


    def delete(self, request, pk,):
        stu = self.get_object(pk)
        stu.delete()
        return Response(deleted_data("Data successfully deleted"),status=NO_CONTENT)


    



# Nested Serializer
class stu(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class prof(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# Nested Serializer  
class Stu_nested(APIView):
    def get(self, request):
        stu = Profile.objects.all()
        serializer = ProfileSerializer(stu, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(success_added("Data successfully inserted",serializer.data),status=CREATED)
        return Response(data_fail("Data Invalid",serializer.errors),status=BAD_REQUEST)
    
    
    
 ############# Country    
class add_country(APIView):
    def get(self,request):
        cou=Country.objects.all()
        serializer =CountrySerializer(cou,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(success_added("Country successfully inserted",serializer.data),status=CREATED)
        return Response(data_fail("Data Invalid",serializer.errors),status=BAD_REQUEST)
    
class country(APIView):
    def get_object(self,pk):
        try:
            return Country.objects.get(pk=pk)
        except Country.DoesNotExist:
            raise Http404
        
    def get(self,request,pk):
        co=self.get_object(pk)
        serializer=CountrySerializer(co)
        return Response(serializer.data)
    
    def put(self,request,pk):
        co=self.get_object(pk)
        serializer = CountrySerializer(co,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(update_data("Country successfully updated",serializer.data),status=OK)
        return Response(data_fail("Update Invalid",serializer.errors),status=BAD_REQUEST)
    
    def patch(self,request,pk):
        co=self.get_object(pk)
        serializer=CountrySerializer(co,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(update_data("Country Successfully Updated",serializer.data),status=OK)
        return Response(data_fail("Update Invalid",serializer.errors),status=BAD_REQUEST)
    
    def delete(self, request, pk,):
        co = self.get_object(pk)
        co.delete()
        return Response(deleted_data("Country successfully deleted"),status=NO_CONTENT)   

       
############### State 
class add_state(APIView):
    def get(self,request):
        st=State.objects.all()
        serializer =StateSerializer(st,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = StateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(success_added("Country successfully inserted",serializer.data),status=CREATED)
        return Response(data_fail("Data Invalid",serializer.errors),status=BAD_REQUEST)
       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
 #Searching Data in Forms  
def search(request):
    # if request.method =="POST":
        name=request.POST['name']
        stu=Student.objects.filter(name__icontains=name)
        context={"stu":stu}
        return render(request,'app/studentdetails.html',context)


    
    


    
    
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
    
#     @login_required(login_url='login_view')
# @csrf_exempt 
# @api_view(['GET','POST','PUT','DELETE'])
# #@permission_classes((IsAuthenticated, ))
# def student_detail(request):
#     if request.method == 'GET':
#         # j_data =request.body
#         # stream = io.BytesIO(j_data)
#         # pythondata=JSONParser().parse(stream)
#         # id = pythondata.get('id', None)
#         # if id is not None:
#         #     stu=Student.objects.get(id=id)
#         #     serializer=StudentSerializer(stu, many=True)
#         #     return Response(serializer.data)
#         stu=Student.objects.all()
#         serializer=StudentSerializer(stu, many=True)
#         return Response(serializer.data)
    
        
# # #insert data    
#     if request.method == 'POST':
#         j_data=request.body
#         stream = io.BytesIO(j_data)
#         pythondata=JSONParser().parse(stream)
#         serializer=StudentSerializer(data =pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res= {'msg':'Data Inserted'}
#             j_data=JSONRenderer().render(res)
#             return HttpResponse(j_data)
#         j_data=JSONRenderer().render(serializer.errors)
#         return HttpResponse(j_data)


# #update_data
#     if request.method == 'PUT':
#         j_data=request.body
#         stream = io.BytesIO(j_data)
#         pythondata=JSONParser().parse(stream)
#         id=pythondata.get('id')
#         stu=Student.objects.get(id=id)
#         serializer=StudentSerializer(stu,data =pythondata,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res= {'msg':'Data Updated'}
#             j_data=JSONRenderer().render(res)
#             return HttpResponse(j_data)
#         j_data=JSONRenderer().render(serializer.errors)
#         return HttpResponse(j_data)
    
       
# #delete
#     if request.method == 'DELETE':
#         j_data=request.body
#         stream = io.BytesIO(j_data)
#         pythondata=JSONParser().parse(stream)
#         id=pythondata.get('id')
#         stu=Student.objects.get(id=id)
#         stu.delete()
#         res= {'msg':'Data Deleted'}
#         return JsonResponse(res,safe=False)
#         # j_data=JSONRenderer().render(res)
#         # return HttpResponse(j_data)

    
    
    
    
    
    
    
    
    
