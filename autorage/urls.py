from django.urls import path
from . import views

app_name = "autorage"

urlpatterns = [
    path('', views.indexViev, name="index"),
    path('car/<int:pk>', views.CarView.as_view(), name="car")
]