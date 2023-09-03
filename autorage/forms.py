from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

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

        self.fields['brand'].widget.attrs.update({'class':'input-box'})
        self.fields['model'].widget.attrs.update({'class':'input-box'})
        self.fields['description'].widget.attrs.update({'class':'input-box'})
        self.fields['modules'].widget.attrs.update({'class':'input-box'})
        self.fields['photo'].widget.attrs.update({'class':'input-box'})

    class Meta:
        model = Car
        fields = ['brand', 'model', 'description', 'modules', 'photo']
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'cols': 60,
                    'rows': 14,
                }
            )
        }

class AutorageCreateUserForm(UserCreationForm):

    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(
            attrs={
                'class': 'input-box'
            }
        )
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.TextInput(
            attrs={
                'class': 'input-box'
            }
        )
    )
    password2 = forms.CharField(
        label='Подтвердите пароль',
        widget=forms.TextInput(
            attrs={
                'class': 'input-box'
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class AutorageAuthenticationForm(AuthenticationForm):

    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(
            attrs={
                'class': 'input-box'
            }
        )
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.TextInput(
            attrs={
                'class': 'input-box'
            }
        )
    )

class AddCommentForm(forms.Form):
    
    text = forms.CharField(
        max_length=255,
        widget=forms.Textarea(
            attrs={
            'cols': 30,
            'rows': 3,
            'class': 'input-box'
            }
        )
    )