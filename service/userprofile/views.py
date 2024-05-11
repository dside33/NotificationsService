from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string

from .models import Profile, APIKey


@login_required
def generate_api_key(request):
    new_key = APIKey.objects.create(user=request.user, value=get_random_string(length=32))

    return redirect('profile')


@login_required
def profile_view(request):
    
    api_keys = APIKey.objects.filter(user=request.user)

    if request.method == 'POST':
        generate_api_key(request)
    
    return render(request, 'profile/profile.html', {'api_keys': api_keys})
    
