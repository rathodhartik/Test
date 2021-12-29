"""finalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='CRUD API')


urlpatterns = [
    # # Base and homepage
    # path('doc',schema_view),
    # # path('base1', views.base1, name='base1'),
    path('home', views.home, name='home'),
    path('', views.homepage, name='homepage'),
    
    # #CRUD API
    #path('student_detail/', views.student_detail, name='student_detail'),
    path('student_detail/', views.student_list.as_view(),name='student_detail'),
    path('student_detail/<int:pk>/', views.student_detail.as_view()),
    
    
    # # Authentication Token
    path('create_token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),
    # #Searching Data in Forms
    path('search', views.search, name='search'),

    
    # # Password Forgot
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name="app/password_reset.html"),name='password_reset'),
    path('password_reset/done',auth_views.PasswordResetDoneView.as_view(template_name="app/password_reset_sent.html"),name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="app/password_reset_form.html"),name='password_reset_confirm'),
    path('password_reset/complete',auth_views.PasswordResetCompleteView.as_view(template_name="app/password_reset_done.html"),name='password_reset_complete'),
]








 #    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQwMzI1MDUxLCJpYXQiOjE2NDAzMjQ3MjksImp0aSI6IjU4YzA2OGMyMmNhYjQ1MmJhN2YyMThjMjI4NTI5YTUyIiwidXNlcl9pZCI6MTB9.xNXH_X_Cr-yLMrP8oBXTZOlbM5EdUvb5ZYhslk5bflk"