from django import forms
from django.forms import ModelForm
from .models import *


class csinfoForm(forms.ModelForm):

    class Meta:
        model = csinfo
        fields = '__all__'