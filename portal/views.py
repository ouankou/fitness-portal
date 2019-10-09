import json
from django.http import HttpResponseBadRequest, JsonResponse
from django.contrib.auth import logout as user_logout, authenticate, login as user_login
from django.shortcuts import render, redirect


def index(request, **kwargs):
    if not request.user.is_authenticated:
        return render(request, "welcome.html")
    else:
        return render(request, "index.html")


def trainer_application(request, **kwargs):
    return render(request, "signups/trainer.html")


def client_signup(request, **kwargs):
    return render(request, "signups/client.html")


def login(request, **kwargs):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None: user_login(request, user)
        return JsonResponse({"is_authenticated": True if user else False})
    else:
        return HttpResponseBadRequest()


def logout(request, **kwargs):
    user_logout(request)
    return redirect("/")
