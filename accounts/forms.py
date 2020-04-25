from django import forms
from accounts.models import UserProfileInfo
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
    password1 = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput())
    
    class Meta():
        model = User
        fields = ('username', 'password', 'password1', 'email')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError("Email address must be unique")
        return email

    def clean_password1(self):
        password = self.cleaned_data.get('password')
        password1 = self.cleaned_data.get('password1')
        if not password or not password1:
            raise ValidationError("Please confirm your password!")
        if password != password1:
            raise ValidationError("Your passwords don't match!")
        return password1


class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('portfolio_site','profile_pic')


class UserLoginForm(forms.Form):
    """Form to be used to log users in"""

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)