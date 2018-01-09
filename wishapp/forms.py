from django.forms import ModelForm
from wishapp.models import Desire
from django import forms
import datetime

class DesireForm(ModelForm):
    class Meta:
        model = Desire
        fields = ['desire_title', 'desire_text']

class DreamerForm(forms.Form):
    dreamer_form_user_id = forms.IntegerField()
    dreamer_form_desire = forms.CharField(max_length=200)