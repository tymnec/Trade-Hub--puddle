from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'class': 'w-full py-4 px-5 font-light rounded-2xl border:none hover:scale-125 transition ease-in-out duration-1000',
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your Password',
        'class': 'w-full py-4 px-5 font-light rounded-2xl border:none hover:scale-125 transition ease-in-out duration-1000',
    }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'class': 'w-full py-4 px-5 font-light rounded-2xl border:none hover:scale-125 transition ease-in-out duration-1000',
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your Email Address',
        'class': 'w-full py-4 px-5 font-light rounded-2xl border:none hover:scale-125 transition ease-in-out duration-1000',
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your Password',
        'class': 'w-full py-4 px-5 font-light rounded-2xl border:none hover:scale-125 transition ease-in-out duration-1000',
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat Password',
        'class': 'w-full py-4 px-5 font-light rounded-2xl border:none hover:scale-125 transition ease-in-out duration-1000',
    }))