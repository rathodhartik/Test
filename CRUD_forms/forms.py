from django import forms
from django.core.exceptions import ValidationError
from app.models import Student




class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            
        }
    # def clean(self):
    #     age=self.cleaned_data['age']
    #     if age < 100:
    #          raise forms.ValidationError("Age not valid")
    

        

class UpdateForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            
        }
