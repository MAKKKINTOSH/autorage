from django.shortcuts import render
from django.http import HttpRequest
from .models import Car
from django.views import generic

def indexViev(request: HttpRequest):

    context = {
        "cars": Car.objects.all(),
    }

    return render(
        request,
        "autorage/index.html",
        context
    )

class CarView(generic.DetailView):

    model = Car
    template_name = "autorage/car.html"
