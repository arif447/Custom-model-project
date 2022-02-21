from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from Custom_model.models import CreateUser


class CreatUserForm(UserCreationForm):
    class Meta:
        model = CreateUser
        fields = ['email', 'password1', 'password2', 'is_staff', 'is_employee']


class LoginForm(forms.Form):
    email = forms.EmailField(
     widget = forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
