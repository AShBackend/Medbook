from django.shortcuts import render, redirect

from django.contrib import messages

from django.contrib.auth import login, logout

from django.contrib.auth.decorators import login_required

from Doctors.models import Reserver

from . forms import RegisterForm, LoginForm

# ___________________________________________________________________________________________

def Register(request):
    if request.user.is_authenticated:
        return redirect('Home:Home')
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, message="اکانت شما با موفقیت ساخته شد")
            return redirect("Home:Home")
    else:
        form = RegisterForm()
    return render(request, "Accounts/register.html", {"form": form})

# ___________________________________________________________________________________________

def Login(request):
    if request.user.is_authenticated:
        return redirect('Home:Home')
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "با موفقیت لاگین شدی ❤️")
            return redirect("Home:Home")
    else:
        form = LoginForm()
    return render(request, "Accounts/login.html", {"form": form})

# ___________________________________________________________________________________________

@login_required
def Logout(request):
    logout(request)
    messages.info(request, "با موفقیت خارج شدی.")
    return redirect("Home:Home")

# ___________________________________________________________________________________________

@login_required
def My_Profile(request):
    appointments = Reserver.objects.filter(Name=request.user)
    return render(request, "Accounts/profile.html", {"appointments": appointments})