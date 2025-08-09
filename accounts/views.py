from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User  # Import User model
from django.contrib.auth.forms import AuthenticationForm

def register_views(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Check if username already exists in User model, not AuthenticationForm
        if User.objects.filter(username=username).exists():
            context = {
                "error": "Username already exists!"
            }
            return render(request, "accounts/register.html", context)

        # Create new user
        User.objects.create_user(username=username, password=password)

        return redirect("login")

    return render(request, "accounts/register.html")


def login_views(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request=request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("task_list")  # ✅ Go to home page after login
        else:
            context = {
                "error": "Invalid Username or password!"
            }
            return render(request, "accounts/login.html", context)

    return render(request, "accounts/login.html")



def logout_views(request):
    logout(request)
    return redirect("login")

