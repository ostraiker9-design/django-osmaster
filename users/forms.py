from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label='Enter your Email',
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'example@gmail.com'
        })
    )

    username = forms.CharField(
        label='Enter your username',
        required=True,
        help_text='Do not use symbols like: @, /',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'user123'
        })
    )

    password1 = forms.CharField(
        label='Set new password',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text='Your password must contain at least 8 characters'
    )

    password2 = forms.CharField(
        label='Confirm password',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# -----------------------------

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label='Enter your Email',
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'example@gmail.com'
        })
    )

    username = forms.CharField(
        label='Enter your username',
        required=True,
        help_text='Do not use symbols like: @, /',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'user123'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email']


# -----------------------------

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['gender', 'allow_mailing']

        widgets = {
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'allow_mailing': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


# -----------------------------

class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(
        label="Load photo",
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Profile
        fields = ['img']