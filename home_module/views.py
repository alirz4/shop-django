from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout

from home_module.forms import UserRegisterForm, UserLoginForm
from home_module.models import User


class HomeView(View):
    template_name = ''

    def get(self, request):
        return render(request, self.template_name)


class UserRegisterView(View):
    template_name = ''
    form_class = UserRegisterForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(phone_number=cd['phone_number'], email=cd['email'], full_name=cd['full_name'],
                                     password=cd['password'])
            messages.success(request, 'successfully created', 'success')
            return redirect('home_module:index')
        else:
            messages.error(request, 'wrong data', 'danger')
        return render(request, self.template_name, {'form': form})


class UserLoginView(View):
    template_name = ''
    form_class = UserLoginForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.filter(phone_number=cd['phone_number']).first()
            if user:
                check = user.check_password(cd['password'])
                if check:
                    login(request, user)
                    messages.success(request, 'logged in')
                    return redirect('home_module:index')
                else:
                    messages.error(request, 'incorrect data')
            else:
                messages.error(request, 'incorrect data')
        else:
            messages.error(request, 'incorrect data')
        return render(request, self.template_name, {'form': form})


class UserLogOutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('home_module:index')
