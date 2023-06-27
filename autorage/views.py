from django.shortcuts import render, redirect
from django.http import HttpRequest, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Car, CarPhoto
from django.views import generic
from config import menu_titles
from .forms import AddPostForm


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


def makePublicationView(request, context):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():

            vals = form.cleaned_data
            brand = form.cleaned_data['brand']
            model = form.cleaned_data['model']
            description = form.cleaned_data['description']
            modules = form.cleaned_data['modules']
            images = form.cleaned_data['image']

            try:
                car = Car.objects.create(
                    brand=brand,
                    model=model,
                    description=description,
                )
                car.modules.set(modules)
                car.carphoto_set.create(photo=images)

            except Exception as e:
                form.add_error(None, "Публикация не создана из-за возникшей ошибки")
                print(f"Ошибка: {e}")
            else:
                return redirect('autorage:succes_post_addition')

        else:
            print(form.errors)

    else:
        form = AddPostForm()

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


class CarView(generic.DetailView):
    model = Car
    template_name = "autorage/car.html"
