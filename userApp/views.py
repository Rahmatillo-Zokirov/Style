from django.shortcuts import render
from django.views import View


class LoginView(View):
    def get(self, request):
        return render(request, 'page-index-2.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'page-user-register.html')
