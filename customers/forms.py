from django import forms  
from .models import Request
    
# creating a form   
class RequestForm(forms.ModelForm):  
    
    class Meta: 
        model = Request 
        fields = "name", "email", "phone", "service", "file", "description"
    