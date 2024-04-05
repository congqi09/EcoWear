import logging

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db import connection
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse


from mypage.forms import ItemForm, SignUpForm, UserProfileForm, BidForm
from mypage.models import User, Item, Favorite, Bid

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
def user_profile(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        return render(request, 'users/user_profile.html', {'user': user})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


@login_required
def edit_user_profile(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        if request.method == 'POST':
            form = UserProfileForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return render(request, 'users/user_profile.html', {'user': user})
        else:
            form = UserProfileForm(instance=user)
        return render(request, 'users/user_form.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


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
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'auction_list.html')
    else:
        form = ItemForm()
    return render(request, 'add_item.html', {'form': form})


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

def item_detail(request, item_id):
    item = get_object_or_404(Item, itemid=item_id)
    favorite_item_ids = Favorite.objects.filter(user=request.user).values_list('item__itemid', flat=True)
    is_favorited = item_id in favorite_item_ids
    bids = item.bids.all()
    highest_bid = bids.first() if bids else None
    bid_form = BidForm()


    if request.method == 'POST':
        bid_form = BidForm(request.POST)
        if bid_form.is_valid():
            new_bid = bid_form.save(commit=False)
            new_bid.item = item
            new_bid.user = request.user
            if not highest_bid or new_bid.amount > highest_bid.amount:
                new_bid.save()
                return redirect('item_detail', item_id=item_id)
            else:
                bid_form.add_error('amount', 'Bid must be higher than current highest bid.')


    return render(request, 'item_detail.html', {'item': item, 'is_favorited': is_favorited, 'highest_bid': highest_bid,
        'bid_form': bid_form})

def toggle_favorite(request, item_id):
    item = get_object_or_404(Item, itemid=item_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, item=item)
    if created:
        messages.success(request, "Item added to favorites.")
    else:
        favorite.delete()
        messages.success(request, "Item removed from favorites.")
    return HttpResponseRedirect(reverse('item_detail', args=[item_id]))

def my_favorites(request):
    user = request.user
    favorites = Favorite.objects.filter(user=user).select_related('item')
    return render(request, 'my_favorites.html', {'favorites': favorites})



