from django.shortcuts import render , redirect
from . import forms 
from django.contrib.auth import authenticate , login ,logout 
from django.conf import settings
# Create your views here.

from django.views.generic import View


class LoginPageView(View):
    template_name = 'authentification/login.html'
    form_class = forms.LoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})
        
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        message = 'Identifiants invalides.'
        return render(request, self.template_name, context={'form': form, 'message': message ,"title":"login"})

def signup_page(request):
    form = forms.SignupForm()
    if request == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request,"authentification/signup.html" , context={'form':form , "title":"signup"})

def logout_user(request):
    logout(request)
    return redirect('login')