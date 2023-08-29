from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpRequest, Http404, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from .models import Car
from django.views import generic
from .utils import menu_titles, DataMixin
from .forms import AddPostForm

class IndexView(DataMixin, generic.ListView):
    """Представление главной страницы"""

    model = Car
    template_name = 'autorage/index.html'
    context_object_name = 'pictures'
    ordering = '?'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:

        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        default_context = self.get_menu_context(self.request.user.is_authenticated, selected_title='')
        return dict(list(context.items()) + list(default_context.items()))


class CarView(DataMixin, generic.DetailView):
    """Представление одной публикации"""

    model = Car
    template_name = "autorage/car.html"
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:

        context = super().get_context_data(**kwargs)
        context['title'] = self.get_object()
        default_context = self.get_menu_context(self.request.user.is_authenticated)
        return dict(list(context.items()) + list(default_context.items()))


class MakePublicationView(DataMixin, generic.CreateView):
    """Представление страницы создания публикации"""

    template_name = 'autorage/add_post.html'
    form_class = AddPostForm
    success_url = reverse_lazy('autorage:index')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:

        context = super().get_context_data(**kwargs)
        context['title'] = 'Опубликовать'
        default_context = self.get_menu_context(self.request.user.is_authenticated, selected_title='make_publication')
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
        default_context = self.get_menu_context(self.request.user.is_authenticated, selected_title='publications')
        return dict(list(context.items()) + list(default_context.items()))

class RegistrationView(DataMixin, generic.CreateView):
    """Представление страницы регистрации"""

    template_name = 'autorage/registration.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        default_context = self.get_menu_context(self.request.user.is_authenticated, selected_title='registration')
        return dict(list(context.items()) + list(default_context.items()))

class AuthenticationView(DataMixin, generic.edit.FormView):
    """Представление страницы входа в профиль"""

    template_name = 'autorage/authentication.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:

        context = super().get_context_data(**kwargs)
        context['title'] = 'Войти'
        default_context = self.get_menu_context(self.request.user.is_authenticated, selected_title='authentication')
        return dict(list(context.items()) + list(default_context.items()))

class ProfileView(DataMixin, generic.DetailView):
    """Представление страницы профиля"""

    template_name = 'autorage/profile.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:

        context = super().get_context_data(**kwargs)
        context['title'] = 'Профиль'
        default_context = self.get_menu_context(self.request.user.is_authenticated, selected_title='profile')
        return dict(list(context.items()) + list(default_context.items()))

def indexView(request: HttpRequest):
    pictures = CarPhoto.objects.all().order_by('?')

    context = {
        'menu_titles': menu_titles,
        'selected_title': 'menu',
        'pictures': pictures,
    }

    return render(
        request,
        "autorage/index.html",
        context
    )


def profileView(request, context):
    return render(
        request,
        "autorage/profile.html",
        context
    )


def makePublicationView(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()
            return redirect('index')

    else:
        form = AddPostForm()

    return render(
        request,
        "autorage/add_post.html",
        {'form': form}
    )


def postsView(request, context):
    return render(
        request,
        "autorage/posts.html",
        context
    )


def searchMainPage(request: HttpRequest, title):
    if title == "menu":
        return HttpResponseRedirect(reverse('autorage:index'))

    context = {
        'menu_titles': menu_titles,
        'selected_title': title
    }
    if title == "posts":
        context['cars'] = Car.objects.all()
        return postsView(request, context)

    if title == "make_publication":
        return makePublicationView(request, context)

    if title == "profile":
        return profileView(request, context)


def mainView(request: HttpRequest, menu_title):
    if menu_title in menu_titles:
        return searchMainPage(request, menu_title)

    else:
        raise Http404()


def PostDoneView(request: HttpRequest):
    return render(request,
                  'autorage/post_done.html',
                  {}
                  )

