from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

from mypage.models import Auction, Item, User, Bid, Message

# If you're using a custom user model, ensure to reference it correctly
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'email', 'address', 'phone']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description', 'image', 'size', 'brand']

class AuctionForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = ['startprice', 'endtime']

class LoginForm(AuthenticationForm):
    pass

class BidForm(forms.ModelForm):
    amount = forms.DecimalField(label='Enter Price', decimal_places=2, max_digits=10, 
                                widget=forms.NumberInput(attrs={
            'placeholder': 'Enter Price in USD', 
            'id': 'bidAmount'  # Directly specifying the id attribute here
        }))
    
    class Meta:
        model = Bid
        fields = ["amount"]


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
