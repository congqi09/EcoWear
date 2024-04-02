from django.contrib import admin
from django.urls import path
from mypage.views import getItemList, getAuctionList, getBidList, signup_view, login_view, home_view

urlpatterns = [
    path('', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('item/', getItemList, name='item_list'),
    path('auction/', getAuctionList, name='auction_list'),
    path('bid/', getBidList, name='bid_list'),
]
