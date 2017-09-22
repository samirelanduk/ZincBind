from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def home_page(request):
    return render(request, "home.html")


def about_page(request):
    return render(request, "about.html")


def help_page(request):
    return render(request, "help.html")


def changelog_page(request):
    return render(request, "changelog.html")


def login_page(request):
    if request.method == "POST":
        user = authenticate(
         username=request.POST["username"],
         password=request.POST["password"]
        )
        if user:
            login(request, user)
            return redirect("/")
        else:
            return render(
             request, "login.html", {"error": "Credentials incorrect"}
            )
    return render(request, "login.html")


def logout_page(request):
    logout(request)
    return redirect("/")
