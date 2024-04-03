from django.urls import path
from mypage.views import edit_item, getItemList, getAuctionList, getBidList, signup_view, login_view, home_view, user_profile, edit_user_profile

urlpatterns = [
    path('', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('user_profile/<int:user_id>/', user_profile, name='user_profile'),
    path('user_profile/<int:user_id>/edit/', edit_user_profile, name='edit_user'),
    path('home/<int:user_id>/', home_view, name='home'),
    path('item/', getItemList, name='item_list'),
    path('item/<int:item_id>/edit/', edit_item, name='edit_item'),
    path('auction/', getAuctionList, name='auction_list'),
    path('bid/', getBidList, name='bid_list'),
]
