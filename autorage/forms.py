from django import forms
from .models import *
from django.forms import inlineformset_factory

# class AddPostForm(forms.Form):
#     brand = forms.ModelChoiceField(
#         queryset=CarBrand.objects.all(),
#         label="Производитель",
#     )
#     model = forms.ModelChoiceField(
#         queryset=CarModel.objects.all(),
#         label="Модель",
#     )
#     description = forms.CharField(
#         widget=forms.Textarea(
#             attrs={'cols': 60, 'rows':10}
#         ),
#         label='Описание'
#     )
#     modules = forms.ModelMultipleChoiceField(
#         queryset=Module.objects.all(),
#         widget=forms.CheckboxSelectMultiple
#     )
#     image = forms.ImageField(
#         label="Изображение"
#     )

class AddPostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['brand'].empty_label = 'Выберите производителя'
        self.fields['model'].empty_label = 'Выберите модель'

    class Meta:
        model = Car
        fields = ['brand', 'model', 'description', 'modules', 'photo']
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'cols': 60,
                    'rows': 14
                }
            )
        }