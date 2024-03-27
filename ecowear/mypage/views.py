from django.db import connection
from django.shortcuts import render

# Create your views here.
def getItemList(request):
    cursor = connection.cursor()
    cursor.execute('''SELECT itemId, title, description, image FROM Item''')
    rows = cursor.fetchall()
    context = {
        "data" : rows
    }
    return render(request, 'item_list.html', context)

def getAuctionList(request):
    cursor = connection.cursor()
    cursor.execute('''SELECT auctionId, itemId, sellerId, buyerId, status, startPrice, currentBid, buyNowPrice, postDate, endDate FROM Auction''')
    rows = cursor.fetchall()
    context = {
        "data" : rows
    }
    return render(request, 'auction_list.html', context)

def getBidList(request):
    cursor = connection.cursor()
    cursor.execute('''SELECT bidId, auctionId, bidderId, bidAmount, bidTime FROM Bid''')
    rows = cursor.fetchall()
    context = {
        "data" : rows
    }
    return render(request, 'bid_list.html', context)