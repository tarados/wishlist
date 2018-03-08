from django.forms import ModelForm
from wishapp.models import Desire
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class DesireForm(ModelForm):
    class Meta:
        model = Desire
        fields = ['desire_title', 'desire_text']


class DreamerForm(forms.Form):
    dreamer_form_user_id = forms.IntegerField()
    dreamer_form_desire = forms.CharField(max_length=200)


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(strip=False, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(strip=False, widget=forms.PasswordInput(attrs={'placeholder': 'Password again'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username',)

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'})}