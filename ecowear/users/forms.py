# users/forms.py

from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'firstName', 'lastName', 'email', 'password', 'address', 'phone', 'profilePicture', 'userGroup', 'userRating', 'registerDate', 'lastLoginDate']
        widgets = {
            'password': forms.PasswordInput(),  # Hide password input
        }
