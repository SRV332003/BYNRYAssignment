from django import forms  
from .models import Request
    
# creating a form   
class RequestForm(forms.ModelForm):  
    
    class Meta: 
        model = Request 
        fields = "name", "email", "phone", "service", "file", "description"

    def clean_data(self):
        name = self.cleaned_data.get('name')
        email = self.cleaned_data.get('email')
        phone = self.cleaned_data.get('phone')
        service = self.cleaned_data.get('service')
        file = self.cleaned_data.get('file')
        message = self.cleaned_data.get('message')

        if not name:
            raise forms.ValidationError('This field is required')
        if not email:
            raise forms.ValidationError('This field is required')
        if not phone:
            raise forms.ValidationError('This field is required')
        if not service:
            raise forms.ValidationError('This field is required')
        if not file:
            raise forms.ValidationError('This field is required')
        if not message:
            raise forms.ValidationError('This field is required')
        return self.cleaned_data
    
