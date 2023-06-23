from django.urls import path
from . import views

app_name = "autorage"

urlpatterns = [
    path('', views.indexView, name="index"),
    path('<str:menu_title>', views.mainView, name='main'),
    path('car/<int:pk>', views.CarView.as_view(), name="car")
]