from django import forms
from . models import Contact

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ["Name", "Email", "Subject", "Text"]

        widgets = {
                'Name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name',
            }),
        
                'Email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
            }),

                'Subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subject',
            }),

                'Text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text',
            }),
        }
