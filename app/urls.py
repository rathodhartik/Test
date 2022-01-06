
from django.db import router
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers
from .views import CityAPI, CountryAPI, city, stu,prof

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='CRUD API')

router = routers.DefaultRouter()
router.register('city', CityAPI, basename='city')

urlpatterns = [
    # # Base and homepage
    # path('doc',schema_view),
    path('base1', views.base1, name='base1'),
    path('home', views.home, name='home'),
    path('', views.homepage, name='homepage'),
    
    
    
    # #CRUD API
    #path('student_detail/', views.student_detail, name='student_detail'),
    path('student_detail/', views.student_list.as_view(),name='student_detail'),
    path('student_detail/<int:pk>/', views.student_detail.as_view()),



    # Nested Serializer
    path('Stu_nested/', views.Stu_nested.as_view(),name='Stu_nested'),
    path('stu',stu.as_view()),
    path('prof',prof.as_view()),
    
    # Country Serializer get,post,put,patch,delete
    path('CountryAPI/', views.CountryAPI.as_view(),name='CountryAPI'),
    path('CountryAPI/<int:pk>/', views.country.as_view()),
    
    
    # City Serializer get,post,put,patch,delete
    path('city/<int:pk>/', views.city.as_view()),
    
    

   # profile AJAX
    path('profile_add/', views.profile_add, name='profile_add'),
    path('profile_add/<int:pk>/', views.profile_update_view, name='profile_change'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
  
  
    

    # # Authentication Token
    path('create_token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),
    
    
    #Searching Data in Forms
    path('search', views.search, name='search'),

    
    #  Password Forgot
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name="app/password_reset.html"),name='password_reset'),
    path('password_reset/done',auth_views.PasswordResetDoneView.as_view(template_name="app/password_reset_sent.html"),name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="app/password_reset_form.html"),name='password_reset_confirm'),
    path('password_reset/complete',auth_views.PasswordResetCompleteView.as_view(template_name="app/password_reset_done.html"),name='password_reset_complete'),
]



urlpatterns += router.urls





 