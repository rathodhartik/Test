from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from app.models import City, Profile




class CreateUserForm(UserCreationForm):
    class Meta:
        model =User
        fields=['username','email','password1','password2']
        


#Profile Form  
class ProfileForm(forms.ModelForm):
    class Meta:
        model =Profile
        fields="__all__"
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass 
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')
    
    
    
    # Validation Firstname and Lastname should not be same
    def clean(self):
        firstname = self.cleaned_data['firstname']
        lastname = self.cleaned_data['lastname']

        if firstname == lastname:
            raise ValidationError("firstname and lastname same")
        
        
    def validate(self):
        name=self.changed_data['name']
        city =City.objects.filter(name__iexact=name)
        
        if city.exists():
            raise ValidationError("taken name")
