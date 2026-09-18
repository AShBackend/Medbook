from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username',
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
            }),

            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].help_text = None
        self.fields["email"].help_text = None
        self.fields["password"].help_text = None



class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Username",
        })

        self.fields["password"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Password",
        })

        self.fields["username"].label = None
        self.fields["password"].label = None