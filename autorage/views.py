from django.shortcuts import render
from django.http import HttpRequest, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Car, CarPhoto
from django.views import generic
from config import menu_titles
from random import shuffle
from .forms import AddPostFrom

def indexView(request: HttpRequest):

    pictures = CarPhoto.objects.all().order_by('?')

    context = {
        'menu_titles': menu_titles,
        'selected_title': 'menu',
        'pictures': pictures,
    }
    print(pictures)

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


def makePublicationView(request, context):

    if request.method == 'POST':
        form = AddPostFrom(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = AddPostFrom()

    context['form'] = form

    return render(
        request,
        "autorage/add_post.html",
        context
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


def mainView(requet: HttpRequest, menu_title):
    if menu_title in menu_titles:
        return searchMainPage(requet, menu_title)

    else:
        raise Http404()


class CarView(generic.DetailView):
    model = Car
    template_name = "autorage/car.html"
