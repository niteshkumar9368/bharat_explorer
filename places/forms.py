from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import TouristPlace
from django.forms.widgets import ClearableFileInput


# 👤 User Registration Form with relaxed validation
class RelaxedUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=150, required=True)

    class Meta:
        model = User
        fields = ("username",)

    def clean_username(self):
        # Allow any username without restrictions
        username = self.cleaned_data.get("username")
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("The two password fields didn’t match.")
        return password2


# 👤 User Registration Form
class CustomUserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


# 🖼️ Custom Widget for Multiple File Upload
class MultipleFileInput(ClearableFileInput):
    allow_multiple_selected = True


# 📍 Tourist Place Form
class TouristPlaceForm(forms.ModelForm):
    gallery_images = forms.FileField(
        widget=MultipleFileInput(attrs={'multiple': True}),
        required=False
    )

    class Meta:
        model = TouristPlace
        fields = [
            'name',
            'description',
            'state',
            'category',
            'image',
            'best_time',
            'location',
            'main_image_url',
        ]
