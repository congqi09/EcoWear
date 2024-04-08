from django.contrib import admin
from django.urls import path
from mypage.views import add_item, getAuctionList, getBidList, signup_view, login_view, home_view, user_profile, edit_user_profile, logout_view, item_detail, toggle_favorite, my_favorites, send_message, message_list, message_detail

urlpatterns = [
    path('', home_view, name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path("logout/", logout_view, name="logout"),
    path('user_profile/', user_profile, name='user_profile'),
    path('user_profile/edit/', edit_user_profile, name='edit_profile'),
    path('home/', home_view, name='home'),
    path('auction/', getAuctionList, name='auction'),
    path('bid/', getBidList, name='bid'),
    path('item/<int:item_id>/', item_detail, name='item_detail'),
    path('item/<int:item_id>/toggle_favorite/', toggle_favorite, name='toggle_favorite'),
    path('my_favorites/', my_favorites, name='my_favorites'),
    path('item/add/', add_item, name='add_item'),
    path('send_message/<int:receiver_id>/<int:item_id>/', send_message, name='send_message'),
    path('messages/', message_list, name='messages'),
    path('message_detail/<int:message_id>/', message_detail, name='message_detail'),
    # Add other URLs as needed
]
