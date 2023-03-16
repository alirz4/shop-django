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
