from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from django.views import View
from django.contrib.auth import login, logout

from home_module.forms import UserRegisterForm, UserLoginForm, ForgetPasswordForm, ResetPasswordForm, \
    VerifyForgetPasswordForm
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


class ForgetPasswordView(View):
    form_class = ForgetPasswordForm
    template_name = ''

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            msg = get_random_string(72)
            request.session['forget_code'] = msg
            request.session.save()
            send_mail('Reset Password', msg, settings.EMAIL_HOST_USER, [email, ], fail_silently=False)
            # todo: redirect to reset pass page
            return redirect('')
        return render(request, self.template_name, {'form': form})


class VerifyForgetPasswordView(View):
    template_name = ''
    form_class = VerifyForgetPasswordForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            if form.cleaned_data['code'] == request.session['forget_code']:
                request.session['reset-pass-true'] = True
                return redirect('')
            else:
                messages.error(request, 'invalid code', 'danger')
        return render(request, self.template_name, {'form': form})


class ResetPasswordView(View):
    template_name = ''
    form_class = ResetPasswordForm

    def dispatch(self, request, *args, **kwargs):
        if request.session['reset-pass-true']:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('home_module:index')

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid:
            request.user.set_password(form.cleaned_data['password'])
            request.user.save()
            messages.success(request, 'successfully changed', 'success')
            return redirect('home_module:log_in')
        return render(request, self.template_name, {'form': form})
