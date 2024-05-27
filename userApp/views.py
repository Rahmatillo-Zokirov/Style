from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views import View

from .models import *
class LoginView(View):
    def get(self, request):
        return render(request, 'page-user-login.html')

    def post(self, request):
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is not None:
            login(request, user)
            return redirect('home')
        return redirect('login')


class RegisterView(View):
    def get(self, request):
        return render(request, 'page-user-register.html')


class UserDetailsView(View):
    def get(self, request):
        if request.user.is_authenticated:
            context = {
                'user': request.user
            }
            return render(request, 'page-profile-main.html')
        return redirect('login')