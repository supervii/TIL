from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import CustomUserCreationForm
from movies.models import Movie

# Create your views here.
def signup(request):
    if request.user.is_authenticated: 
        return redirect('accounts:user_list')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts:user_list')
    else:
        form = CustomUserCreationForm()
    context = {'form': form,}
    return render(request, 'accounts/auth_form.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:user_list')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'accounts:user_list')
    else:
        form = AuthenticationForm()
    context = {'form': form,}
    return render(request, 'accounts/auth_form.html', context)


def logout(request):
    auth_logout(request)
    return redirect('accounts:user_list')


def user_list(request):
    users = User.objects.all()
    context = {'users': users,}
    return render(request, 'accounts/user_list.html', context)


def user_detail(request, user_pk):
    users = get_object_or_404(get_user_model(), pk=user_pk)
    reviews = users.review_set.all()
    context = {'users': users, 'reviews': reviews,}   
    return render(request, 'accounts/detail.html', context)