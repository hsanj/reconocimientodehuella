from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django import forms
from .models import Queja

class QuejaForm(forms.ModelForm):
    class Meta:
        model = Queja
        fields = '__all__'
        widgets = {
            'DesQueja': forms.Textarea(attrs={'class': 'textarea','rows':5})
        }