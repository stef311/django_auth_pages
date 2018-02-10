from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegistrationForm

# Create your views here.


def validate_username(request):
    username = request.GET.get('username', None)
    print(username)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()

            return redirect("users:user_login")
        else:
            return HttpResponse("Form not valid")

    else:
        user_form = UserRegistrationForm()
        return render(request, "users/register.html", {"user_form": user_form})

def user_login(request):
    if request.method == "POST":
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            cd = user_form.cleaned_data
            user = authenticate(username=cd["username"],
                                password=cd["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("users:register")
                else:
                    return HttpResponse("user is not active")
            else:
                return HttpResponse("Invalid Login")
        else:
            return HttpResponse("Not valid form")
    else:
        user_form = UserLoginForm()
        return render(request, "users/login.html", {"user_form": user_form})