
from django import forms
from django.contrib.auth import authenticate,get_user_model,password_validation
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator, FileExtensionValidator



class SignupForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "First Name",
            "class": "form-control"
        }))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "Last Name",
            "class": "form-control"
        }))
    email = forms.EmailField(max_length=200, help_text='Required', widget=forms.EmailInput(attrs={
        "placeholder": "Email",
        "class": "form-control"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Password",
        "class": "form-control"
    }))

    confirmPassword = forms.CharField(label="confirm password", widget=forms.PasswordInput(attrs={
        "placeholder": "Confirm Password",
        "class": "form-control"
    }))
    phone = forms.CharField(label="phone number", validators=[RegexValidator(
        '^01[0125][0-9]{8}$', message="Enter a Valid Egyption Phone Number")], widget=forms.TextInput(attrs={
            "placeholder": "Phone Number",
            "class": "form-control"
        }))
    image = forms.ImageField(label="profile image", validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])], widget=forms.FileInput(attrs={
        "placeholder": "Profile Image",
        "class": "form-control"
    }))

class LoginForm(forms.Form):

        email = forms.EmailField(max_length=200, widget=forms.EmailInput(attrs={
            "placeholder": "Email",
            "class": "form-control"
        }))
        password = forms.CharField(widget=forms.PasswordInput(attrs={
            "placeholder": "Password",
            "class": "form-control"
        }))

