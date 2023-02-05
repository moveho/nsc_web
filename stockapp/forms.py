from django import forms
from django.forms import ModelForm
from django import forms
from stockapp.models import Kospi


class KospiCreationForm(ModelForm):
    class Meta:
        model = Kospi
        fields = '__all__'
        wigets = {
            'date' : forms.DateInput(attrs={'type': 'date'})
        }