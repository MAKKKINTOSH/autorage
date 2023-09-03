from typing import Any, Dict
from django.urls import reverse_lazy
from .models import Car, Comment
from django.views import generic
from .utils import menu_titles, DataMixin
from .forms import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpRequest
from autorage.utils import menu_titles
import re


class IndexView(DataMixin, generic.ListView):
    """Представление главной страницы"""

    model = Car
    template_name = 'autorage/index.html'
    context_object_name = 'pictures'
    ordering = '?'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:

        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        default_context = self.get_menu_context(self.request.user, selected_title='')
        return dict(list(context.items()) + list(default_context.items()))


class CarView(DataMixin, generic.DetailView):
    """Представление одной публикации"""

    model = Car
    template_name = "autorage/car.html"
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:

        this_car = self.get_object()

        context = super().get_context_data(**kwargs)
        context['title'] = this_car
        context['comments'] = Comment.objects.filter(car=this_car)
        default_context = self.get_menu_context(self.request.user)
        return dict(list(context.items()) + list(default_context.items()))
    

def carView(request: HttpRequest, pk: int):

    car = Car.objects.get(pk=pk)

    context = {}
    context['menu_titles'] = menu_titles.copy()
    context['is_auth'] = request.user.is_authenticated
    context['selected_title'] = 'none'
    context['car'] = car
    context['comments'] = Comment.objects.filter(car=car)

    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            
            print(form.cleaned_data)
            text = form.cleaned_data['text']
            author = request.user
            
            try:
                Comment.objects.create(
                    text=text,
                    author=author,
                    car=car
                )
            except Exception as e:
                form.add_error(None, "Публикация не создана из-за возникшей ошибки")
                print(f"Ошибка: {e}")
            else:
                return redirect(car)

        else:
            print(form.errors)
    else:
        form = AddCommentForm()

    context['comment_form'] = form

    return render(
        request,
        'autorage/car.html',
        context
    )

class MakePublicationView(DataMixin, generic.CreateView):
    """Представление страницы создания публикации"""

    template_name = 'autorage/add_post.html'
    form_class = AddPostForm
    success_url = reverse_lazy('autorage:index')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:

        context = super().get_context_data(**kwargs)
        context['title'] = 'Опубликовать'
        default_context = self.get_menu_context(self.request.user, selected_title='make_publication')
        return dict(list(context.items()) + list(default_context.items()))


class PublicationsView(DataMixin, generic.ListView):
    """Представление страницы с публикациями"""

    model = Car
    template_name = 'autorage/posts.html'
    context_object_name = 'cars'
    extra_context = {
        'title': 'Публикации'
    }

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:

        context = super().get_context_data(**kwargs)
        default_context = self.get_menu_context(self.request.user, selected_title='publications')
        return dict(list(context.items()) + list(default_context.items()))

class RegistrationView(DataMixin, generic.CreateView):
    """Представление страницы регистрации"""

    form_class = AutorageCreateUserForm
    template_name = 'autorage/registration.html'
    success_url = reverse_lazy('autorage:index')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        default_context = self.get_menu_context(self.request.user, selected_title='registration')
        return dict(list(context.items()) + list(default_context.items()))

class AuthenticationView(DataMixin, LoginView):
    """Представление страницы входа в профиль"""

    form_class = AutorageAuthenticationForm
    template_name = 'autorage/authentication.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:

        context = super().get_context_data(**kwargs)
        context['title'] = 'Войти'
        default_context = self.get_menu_context(self.request.user, selected_title='authentication')
        return dict(list(context.items()) + list(default_context.items()))
    
    def get_success_url(self) -> str:
        return reverse_lazy('autorage:index')

class ProfileView(DataMixin, generic.DetailView):
    """Представление страницы профиля"""

    template_name = 'autorage/profile.html'
    model = User
    context_object_name = 'user'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:

        context = super().get_context_data(**kwargs)
        context['title'] = 'Профиль'
        default_context = self.get_menu_context(self.request.user, selected_title='profile')
        return dict(list(context.items()) + list(default_context.items()))
