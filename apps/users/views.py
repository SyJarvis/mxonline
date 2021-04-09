from django.shortcuts import render
from django.http import HttpResponse
# 登录认证\登录\登出
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import View
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password

from .models import UserProfile
from .forms import LoginForm, RegisterForm
# Create your views here.


# def login(request):
#     return render(request, 'login.html', {})
class CustomBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(username=username)
            if user.check_password(password):
                return user

        except Exception as e:
            return None

"""
def user_login(request):
    if request.method == "POST":
        user_name = request.POST.get("username", "")
        pass_word = request.POST.get("password", "")
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            login(request, user)
            return render(request, "index.html")
        else:
            return render(request, "login.html", {"msg": "用户名或密码错误"})
    elif request.method == "GET":
        return render(request, 'login.html', {})
"""


class LoginView(View):
    """"""
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            print(request.method)
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            print("sssss")
            print(user_name)
            print(pass_word)
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                print('没登录')
                login(request, user)
                return render(request, 'index.html')
            else:
                return render(request, 'login.html', {"msg": "用户名或者密码错误"})
        else:
            print("login error")
            return render(request, 'login.html', {"login_form": login_form})


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.password = make_password(pass_word)
            user_profile.save()
            pass















