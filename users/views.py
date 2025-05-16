from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
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


def login_user(request):
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            # Check if the user exists
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, "Username not found.")

        #  Authenticate the user or return None
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Creating a session for the user
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "users/login_register.html")


def logout_user(request):
    logout(request)
    return redirect('login')
