from django import forms
from django .forms import ModelForm
from .models import card
class empform(forms.ModelForm):
    class Meta:
        model=card
        fields="__all__"