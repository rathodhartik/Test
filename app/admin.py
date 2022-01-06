from django.contrib import admin
from .models import Student ,Profile,City,Country

# Register your models here.

admin.site.register(Student)
admin.site.register(Profile)
admin.site.register(City)

admin.site.register(Country)

