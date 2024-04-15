import logging

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db import connection
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta

from mypage.forms import AuctionForm, ItemForm, SignUpForm, UserProfileForm, BidForm, MessageForm
from mypage.models import User, Item, Favorite, Bid, Message, Auction

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
    if not request.user.is_authenticated:
        return redirect('login')
    auctions = Auction.objects.filter(status='active')
    auction_list = []
    for auction in auctions:
        auction_list.append({
            'itemid': auction.item.itemid,
            'item_name': auction.item.title,
            'image': auction.item.image if auction.item.image else 'https://via.placeholder.com/150',
            'start_price': auction.startprice,
            'post_date': auction.addtime,
            'end_date': auction.endtime,
            'status': auction.status
        })
    context = {
        "data": auction_list
    }
    return render(request, 'home.html', context)


@login_required
def getAuctionList(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    user_auctions = Auction.objects.filter(seller=request.user)
    auctions_list = []
    for auction in user_auctions:
        current_bid = auction.currentbid()
        buyer = current_bid.user if current_bid else None
        auctions_list.append({
            'itemid': auction.item.itemid,
            'item_name': auction.item.title,
            'buyerid': buyer.userId if buyer else None,
            'buyer': buyer.username if buyer else None,
            'start_price': auction.startprice,
            'current_price': current_bid.amount if current_bid else auction.startprice,
            'addtime': auction.addtime,
            'endtime': auction.endtime,
            'status': auction.status
        })
    context = {
        "data": auctions_list
    }
    return render(request, 'auction_list.html', context)


@login_required
def add_item(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    if request.method == 'POST':
        item_form = ItemForm(request.POST)
        auction_form = AuctionForm(request.POST)
        if item_form.is_valid() and auction_form.is_valid():
            item = item_form.save()
            auction = auction_form.save(commit=False)
            auction.item = item
            auction.seller = user
            auction.buyer = None
            auction.currentBid = None
            auction.status = 'active'
            auction.save()
            return redirect('auction')
    else:
        item_form = ItemForm()
        auction_form = AuctionForm()
    return render(request, 'add_item.html', {'item_form': item_form, 'auction_form': auction_form})


@login_required
def getBidList(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    user_bids = Bid.objects.filter(user=request.user)

    # Prepare data for each bid, including status
    bids_with_status = []
    for bid in user_bids:
        seller = Auction.objects.get(item=bid.item).seller
        bids_with_status.append({
            'itemid': bid.item.itemid,
            'title': bid.item.title,
            'sellerid': seller.userId,
            'seller_username': seller.username,
            'amount': bid.amount,
            'bidTime': bid.bidtime,
            'status': bid.status()  # Now correctly calling the instance method
        })

    context = {
        "data": bids_with_status
    }
    return render(request, 'bid_list.html', context)


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('login')  # Adjust the redirect as needed


@login_required
def item_detail(request, item_id):
    if not request.user.is_authenticated:
        return redirect('login')
    item = get_object_or_404(Item, itemid=item_id)
    favorite_item_ids = Favorite.objects.filter(user=request.user).values_list('item__itemid', flat=True)
    is_favorited = item_id in favorite_item_ids
    bidding_active = item.is_bidding_active()
    bidding_end_time = item.List_time + timedelta(days=5)
    time_remaining = bidding_end_time - timezone.now()
    if time_remaining.total_seconds() > 0:
        time_remaining = time_remaining
    else:
        time_remaining = timedelta(seconds=0)

    bids = item.bids.all()
    highest_bid = bids.first() if bids else None
    bid_form = BidForm()
    message_form = MessageForm()
    auction = get_object_or_404(Auction, item=item)
    seller = auction.seller
    currentBuyerId = auction.currentbid().user.userId if auction.currentbid() else None
    currentBuyer = auction.currentbid().user.username if auction.currentbid() else None
    BidUser = User.objects.get(username=request.user.username)
    message_form_url = reverse('send_message', kwargs={'receiver_id': auction.seller.userId, 'item_id': item.itemid})
    user_is_seller = BidUser == seller
    startPrice = auction.startprice

    if request.method == 'POST':
        bid_form = BidForm(request.POST)
        # message_form = MessageForm(request.POST, prefix='message')

        if bid_form.is_valid():
            new_bid = bid_form.save(commit=False)
            new_bid.item = item
            new_bid.user = request.user
            if user_is_seller: 
                messages.error(request, "You cannot bid on your own auction.")
                return redirect('item_detail', item_id=item_id)
            if new_bid.amount < startPrice:
                bid_form.add_error('amount', 'Bid must be higher than the starting price.')

            if not highest_bid or new_bid.amount > highest_bid.amount:
                new_bid.save()
                return redirect('item_detail', item_id=item_id)
            else:
                bid_form.add_error('amount', 'Bid must be higher than current highest bid.')


    return render(request, 'item_detail.html',
                   {'item': item, 
                    'is_favorited': is_favorited, 
                    'highest_bid': highest_bid,
                    'bid_form': bid_form, 
                    'bidding_active': bidding_active, 
                    'time_remaining': time_remaining, 
                    'bidding_end_time': bidding_end_time,
                    'message_form': message_form,
                    'seller_id': seller.userId,
                    'user_is_seller': user_is_seller,
                    'startPrice': startPrice,
                    'currentBuyerId': currentBuyerId,
                    'currentBuyer': currentBuyer,
                    })

@login_required
def accept_current_bid(request, item_id):
    if not request.user.is_authenticated:
        return redirect('login')
    item = get_object_or_404(Item, itemid=item_id)
    item.currentTime = item.List_time + timedelta(days=10)
    item.save()
    auction = get_object_or_404(Auction, item=item)
    auction.status = 'sold'
    auction.save()

    return redirect('item_detail', item_id=item.itemid)

@login_required
def toggle_favorite(request, item_id):
    if not request.user.is_authenticated:
        return redirect('login')
    item = get_object_or_404(Item, itemid=item_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, item=item)
    if created:
        messages.success(request, "Item added to favorites.")
    else:
        favorite.delete()
        messages.success(request, "Item removed from favorites.")
    return HttpResponseRedirect(reverse('item_detail', args=[item_id]))


@login_required
def my_favorites(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    favorites = Favorite.objects.filter(user=user).select_related('item')
    return render(request, 'my_favorites.html', {'favorites': favorites})


@login_required
def send_message(request, receiver_id, item_id):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            msg = message_form.save(commit=False)
            msg.sender = request.user
            msg.save()
            return redirect('messages')
    else:
        message_form = MessageForm()
    return render(request, 'messaging/send_message.html', {'form': message_form})


@login_required
def send_message(request, receiver_id, item_id):
    if not request.user.is_authenticated:
        return redirect('login')
    receiver = get_object_or_404(User, pk=receiver_id)
    item = get_object_or_404(Item, pk=item_id)  # Assume you need to handle item
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
            msg.receiver = receiver
            msg.item = item 
            msg.save()
            return redirect('messages')
    else:
        # Prepopulate the receiver and item fields if you want
        form = MessageForm(initial={'receiver': receiver, 'item': item})

    context = {
        'form': form,
        'receiver_name': receiver.username,
        'item_name': item.title,  # Assuming your Item model has a 'name' field
    }
    return render(request, 'send_message.html', context)


@login_required
def message_list(request):
    if not request.user.is_authenticated:
        return redirect('login')
    messages = Message.objects.filter(receiver=request.user).order_by('-time_sent')
    return render(request, 'messages.html', {'messages': messages})


@login_required
def message_detail(request, message_id):
    if not request.user.is_authenticated:
        return redirect('login')
    message = get_object_or_404(Message, message_id=message_id, receiver=request.user)
    item = message.item
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.sender = request.user
            reply.receiver = message.sender
            reply.item = item 
            reply.save()
            return redirect('messages')
    else:
        form = MessageForm(initial={'receiver': message.sender})

    context = {
        'form': form,
        'message': message
    }    
    return render(request, 'message_detail.html', context)

