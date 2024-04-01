from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_user, name='create_user'),
    path('<int:user_id>/edit/', views.edit_user, name='edit_user'),
    # path('users/<int:user_id>/', views.user_detail, name='user_detail'),
]
