from django.shortcuts import render
from django.views import View
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.db import IntegrityError
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth import logout

from .forms import SignInForm, SignUpForm
# Create your views here.
class SignUpView(View):
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect("/")
        form = SignUpForm()
        return render(request, "accounts/reg.html", context={"form": form})

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
            except IntegrityError as e:
                return render(request, "accounts/reg.html", context={"form": form, "e": e})
        return HttpResponseRedirect("/")

class SignInView(View):
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect("/")
        form = SignInForm()
        return render(request, "accounts/auth.html", context={"form": form})

    def post(self, request, *args, **kwargs):
        form = SignInForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/")
        return render(request, "accounts/auth.html", context={"form": form})
        
class MainView(View):
        def get(self, request, *args, **kwargs):
            user = self.request.user
            return render(request, "accounts/main.html", context={"user" : user})

class LogOutView(View):
    def post(self, request):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect("/")
        logout(request)
        return HttpResponseRedirect("/")
