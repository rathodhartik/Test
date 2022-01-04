from django import forms
from app.models import Student




class StudentForm(forms.ModelForm):
    
    class Meta:
        model=Student
        fields="__all__"
    
    
   

class UpdateForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
      
