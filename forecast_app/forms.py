from django import forms
from forecast_app.models import UserProfile
from django.contrib.auth.models import User

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


