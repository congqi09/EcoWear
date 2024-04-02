from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

from mypage.models import User

# If you're using a custom user model, ensure to reference it correctly
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'email', 'address', 'phone']

class LoginForm(AuthenticationForm):
    pass
