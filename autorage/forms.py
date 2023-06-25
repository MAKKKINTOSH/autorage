from django import forms
from .models import *

class AddPostFrom(forms.Form):
    brand = forms.ModelChoiceField(
        queryset=CarBrand.objects.all(),
        label="Производитель",
    )
    model = forms.ModelChoiceField(
        queryset=CarModel.objects.all(),
        label="Модель",
    )
    desription = forms.CharField(
        widget=forms.Textarea(
            attrs={'cols': 60, 'rows':10}
        )
    )
    modules = forms.ModelMultipleChoiceField(
        queryset=Module.objects.all(),
    )

