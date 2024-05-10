from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string

from .models import Profile, APIKey


class ProfileView(DetailView):
    model = Profile
    template_name = 'profile/profile.html'


@login_required
def generate_api_key(request):
    new_key = APIKey.objects.create(user=request.user, value=get_random_string(length=32))

    return redirect('profile')


@login_required
def profile(request):
    api_keys = APIKey.objects.filter(user=request.user)

    if request.method == 'POST':
        generate_api_key(request)
    
    return render(request, 'profile.html', {'api_keys': api_keys})
    
