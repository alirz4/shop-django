from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from home_module.models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(max_length=72, label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=72, label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('phone_number', 'email', 'full_name')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError('passwords not match')
        return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=True)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text='you can change password by <a href="../password/">this form</a>')

    class Meta:
        model = User
        fields = '__all__'


class UserRegisterForm(forms.Form):
    phone = forms.CharField(max_length=11, label='Phone Number', widget=forms.TextInput)
    email = forms.EmailField(max_length=50, label='Email', widget=forms.EmailInput)
    full_name = forms.CharField(max_length=40, label='Full Name', widget=forms.TextInput)
    password1 = forms.CharField(max_length=20, label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=20, label='Confirm Password', widget=forms.PasswordInput)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError('passwords not match')
        return cd['password2']


class UserLoginForm(forms.Form):
    phone = forms.CharField(max_length=11, label='Phone Number', widget=forms.TextInput)
    password = forms.CharField(max_length=20, label='Password', widget=forms.PasswordInput)


class ForgetPasswordForm(forms.Form):
    email = forms.EmailField(max_length=100, widget=forms.EmailInput, label='Email')


class VerifyForgetPasswordForm(forms.Form):
    code = forms.CharField(max_length=100, widget=forms.TextInput, label='Code')


class ResetPasswordForm(forms.Form):
    password = forms.CharField(max_length=30, label='password', widget=forms.TextInput)
    confirm_password = forms.CharField(max_length=30, label='confirm password', widget=forms.TextInput)

    def clean_confirm_password(self):
        cd = self.cleaned_data
        if cd['password'] and cd['confirm_password'] and cd['password'] != cd['confirm_password']:
            raise ValidationError('passwords not match')
        return cd['confirm_password']
