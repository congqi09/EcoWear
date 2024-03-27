from django.db import connection
from django.shortcuts import render

# Create your views here.
def getAuctionList(request):
    cursor = connection.cursor()
    cursor.execute('''SELECT itemId, title, description, image FROM Item''')
    rows = cursor.fetchall()
    context = {
        "data" : rows
    }
    return render(request, 'auction_list.html', context)
