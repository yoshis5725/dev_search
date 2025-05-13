from django.shortcuts import render, get_object_or_404
from .models import Profile


def profiles(request):
    all_profiles = Profile.objects.all()
    context = {
        "profiles": all_profiles,
    }
    return render(request, "users/profiles.html", context)


def user_profile(request,pk):
    fetched_profile = get_object_or_404(Profile, pk=pk)
    context = {
        "profile": fetched_profile,
    }
    return render(request, "users/user_profile.html", context)
