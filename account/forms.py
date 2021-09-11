from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account, Profile



class AdminSignUpForm(UserCreationForm):
    class Meta (UserCreationForm.Meta):
        model = Account
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        account = super().save(commit=False)
        account.is_admin = True
        account.is_staff = True

        if commit:
            account.save()
        return account


class WebmasterSignUpForm(UserCreationForm):
    class Meta (UserCreationForm.Meta):
        model = Account
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        account = super().save(commit=False)
        account.is_webmaster = True
        account.is_staff = True

        if commit:
            account.save()
        return account


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Account
        fields = ['username', 'email',]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']