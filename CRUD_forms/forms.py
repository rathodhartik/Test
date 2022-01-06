from django import forms
from django.core.exceptions import ValidationError
from app.models import Student



# Student Form
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            
        }
# Student Update Form
class UpdateForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            
        }
