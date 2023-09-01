from typing import Any, Dict
from django.db import models
from django.urls import reverse_lazy
from .models import Car, Comment
from django.views import generic
from .utils import menu_titles, DataMixin
from .forms import AddPostForm, AutorageCreateUserForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

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

    form_class = AuthenticationForm
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
