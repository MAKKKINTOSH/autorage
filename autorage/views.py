from django.shortcuts import render
from django.http import HttpRequest
from .models import Car

def index(request: HttpRequest):

    context = {
        "cars": Car.objects.all(),
    }

    return render(
        request,
        "autorage/index.html",
        context
    )