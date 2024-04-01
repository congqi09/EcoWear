# users/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm
from .models import User

def user_detail(request, user_id):
    user = User.objects.get(userId=user_id)
    return render(request, 'user_detail.html', {'user': user})

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')  # Redirect to a page that lists users
    else:
        form = UserForm()
    return render(request, 'users/user_form.html', {'form': form})

def edit_user(request, user_id):
    user = get_object_or_404(User, userId=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_detail', user_id=user.userId)  # Redirect to the user's detail view
    else:
        form = UserForm(instance=user)
    return render(request, 'users/user_form.html', {'form': form})
