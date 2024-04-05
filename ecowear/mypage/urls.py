from django.contrib import admin
from django.urls import path
from mypage.views import add_item, getAuctionList, getBidList, signup_view, login_view, home_view, user_profile, edit_user_profile, logout_view, item_detail, toggle_favorite, my_favorites

urlpatterns = [
    path('', home_view, name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path("logout/", logout_view, name="logout"),
    path('user_profile/<int:user_id>/', user_profile, name='user_profile'),
    path('user_profile/<int:user_id>/edit/', edit_user_profile, name='edit_user'),
    path('home/', home_view, name='home'),
    path('auction/', getAuctionList, name='auction'),
    path('bid/', getBidList, name='bid'),
    path('item/<int:item_id>/', item_detail, name='item_detail'),
    path('item/<int:item_id>/toggle_favorite/', toggle_favorite, name='toggle_favorite'),
    path('my_favorites/', my_favorites, name='my_favorites'),
    path('item/add/', add_item, name='add_item'),
]
