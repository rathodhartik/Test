from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Validation Email
def validate_email(value):
    if User.objects.filter(email = value).exists():
        raise ValidationError((f"{value}  already taken."),params = {'value':value})


# Register Form
class SignUpForm(UserCreationForm):
    email = forms.EmailField(validators = [validate_email])
    class Meta:
        model =User
        fields=["username","email","password1","password2"]
        

        
        
        
        
        
