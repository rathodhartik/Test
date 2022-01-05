from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from app.models import Profile




class CreateUserForm(UserCreationForm):
    class Meta:
        model =User
        fields=['username','email','password1','password2']
        
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model =Profile
        fields=['firstname','lastname','age','gender','country','state','city','user']
    
    
    def clean(self):
        firstname = self.cleaned_data['firstname']
        lastname = self.cleaned_data['lastname']

        if firstname == lastname:
            raise ValidationError("firstname and lastname same")
        
        
        
