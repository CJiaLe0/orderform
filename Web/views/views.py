from django.shortcuts import render, reverse
from django import forms


class LoginForm(forms.Form):
    pass


def login(request):

    username = request.POST.get("username")
    print(username)
    password = request.POST.get("password")
    print(password)

    return render(request, "login.html")


def sms_login(request):

    mobile = request.POST.get("mobile")
    print(mobile)
    auth_code = request.POST.get("auth_code")
    print(auth_code)
    code = request.POST.get("code")
    print(code)

    return render(request, "sms_login.html")