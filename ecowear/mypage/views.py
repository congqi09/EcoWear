import logging

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db import connection
from django.shortcuts import render, redirect, get_object_or_404

from mypage.forms import ItemForm, SignUpForm, UserProfileForm
from mypage.models import User, Item

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Create your views here.
def edit_item(request, item_id):
    item = get_object_or_404(Item, itemid=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return render(request, 'item_list.html')
    else:
        form = ItemForm(instance=item)
    return render(request, 'item_edit.html', {'form': form})


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
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        logger.info(f'User {user} has logged in')

        if user is not None:
            login(request, user)
            return redirect('home')
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
def home_view(request):
    if request.user.is_authenticated:
        cursor = connection.cursor()
        cursor.execute('''
            SELECT
                i.itemId,
                i.title,
                i.description,
                i.image
            FROM Auction a LEFT JOIN Item i ON a.itemId = i.itemId'''
            # WHERE a.status = 'active';'''
        )
        rows = cursor.fetchall()
        context = {
            "data": rows
        }
        return render(request, 'home.html', context)
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


@login_required
def getAuctionList(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        cursor = connection.cursor()
        cursor.execute(
            '''SELECT
                i.title, 
                u.username, 
                a.startPrice, 
                a.currentBid, 
                a.postDate, 
                a.endDate,
                a.status
            FROM Auction a LEFT JOIN Item i ON a.itemId = i.itemId
                    LEFT JOIN User u ON a.buyerId = u.userId
            WHERE a.sellerId = ''' + str(user.userId) + ";"
        )
        rows = cursor.fetchall()
        context = {
            "data": rows
        }
        return render(request, 'auction_list.html', context)
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


@login_required
def getBidList(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        cursor = connection.cursor()
        cursor.execute(
            '''SELECT
                i.title,
                u.username,
                b.bidAmount,
                b.bidTime
            FROM Bid b LEFT JOIN Auction a ON b.auctionId = a.auctionId
                LEFT JOIN Item i ON a.itemId = i.itemId
                LEFT JOIN User u ON a.sellerId = u.userId
            WHERE b.bidderId = ''' + str(user.userId) + ";")
        rows = cursor.fetchall()
        context = {
            "data": rows
        }
        return render(request, 'bid_list.html', context)
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('login')  # Adjust the redirect as needed
