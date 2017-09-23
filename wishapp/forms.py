from django.forms import ModelForm
from wishapp.models import Desire
import datetime

class DesireForm(ModelForm):
    class Meta:
        model = Desire
        fields = ['desire_text']