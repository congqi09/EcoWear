import logging
import uuid
from uuid import UUID

from django.urls import reverse
from django.contrib.auth import login, authenticate, get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password, check_password
from django.db import connection
from django.shortcuts import render, redirect, get_object_or_404

from mypage.forms import SignUpForm, LoginForm, UserProfileForm

from mypage.models import User

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Create your views here.
def getItemList(request):
    cursor = connection.cursor()
    cursor.execute('''SELECT itemId, title, description, image FROM Item''')
    rows = cursor.fetchall()
    context = {
        "data": rows
    }
    return render(request, 'item_list.html', context)


def getAuctionList(request):
    cursor = connection.cursor()
    cursor.execute(
        '''SELECT auctionId, itemId, sellerId, buyerId, status, startPrice, currentBid, buyNowPrice, postDate, endDate FROM Auction''')
    rows = cursor.fetchall()
    context = {
        "data": rows
    }
    return render(request, 'auction_list.html', context)


def getBidList(request):
    cursor = connection.cursor()
    cursor.execute('''SELECT bidId, auctionId, bidderId, bidAmount, bidTime FROM Bid''')
    rows = cursor.fetchall()
    context = {
        "data": rows
    }
    return render(request, 'bid_list.html', context)


def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')

        user = User.objects.create_user(email, username, firstname=first_name, lastname=last_name)
        user.set_password(password)
        user.save()
        logger.info(f'User {username} has signed up')

        return redirect('login')

    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        return render(request, 'home.html', {'user': user})
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        logger.info(f'User {user} has logged in')

        if user is not None:
            login(request, user)
            return render(request, 'home.html', {'user': user})
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    
@login_required
def user_profile(request, user_id):
    user = User.objects.get(userId=user_id)
    return render(request, 'users/user_profile.html', {'user': user})

@login_required
def edit_user_profile(request, user_id):
    user = get_object_or_404(User, userId=user_id)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return render(request, 'users/user_profile.html', {'user': user})
    else:
        form = UserProfileForm(instance=user)
    return render(request, 'users/user_form.html', {'form': form})

@login_required
def home_view(request, user_id):
    user = get_object_or_404(User, userId=user_id)
    return render(request, 'home.html', {'user': user})

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('login')  # Adjust the redirect as needed
