from .models import Profile

from django.shortcuts import get_object_or_404


def get_user_profile(request):
    profile = None
    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()

    return {'profile': profile}