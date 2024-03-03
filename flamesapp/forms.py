from django import forms
from .models import contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = "__all__"
        widgets = {
            "first_name" : forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter your first name"}),
            "last_name" : forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter your last name"}),
            "e_mail" : forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter your email"}),
            "phone_number" : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': "Enter your phone number"}),
            "contact_meassage" : forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Enter your meassage "}),


        }