from django.contrib import admin
from django.urls import path
from mypage.views import getItemList, getAuctionList, getBidList, signup_view, login_view, home_view, user_profile, edit_user_profile, logout_view

urlpatterns = [
    path('', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path("logout/", logout_view, name="logout"),
    path('user_profile/<int:user_id>/', user_profile, name='user_profile'),
    path('user_profile/<int:user_id>/edit/', edit_user_profile, name='edit_user'),
    path('home/', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('item/', getItemList, name='item_list'),
    path('auction/', getAuctionList, name='auction_list'),
    path('bid/', getBidList, name='bid_list'),
]