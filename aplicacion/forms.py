from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import Queja

class  QuejaForm(ModelForm):
    class Meta:
        model = Queja
        fields = '__all__'
        widgets = {
            'DesQueja': forms.Textarea(attrs={'class': 'textarea','rows':5} )
        }