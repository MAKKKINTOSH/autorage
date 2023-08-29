from django.urls import path
from . import views

app_name = "autorage"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    # path('<str:menu_title>', views.mainView, name='main'),
    path('make_publication', views.MakePublicationView.as_view(), name='make_publication'),
    path('publications', views.PublicationsView.as_view(), name='publications'),
    path('registration', views.RegistrationView.as_view(), name='registration'),
    path('authentication', views.AuthenticationView.as_view(), name='authentication'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('car/<int:pk>', views.CarView.as_view(), name="car"),
    # path('car/post_done', views.PostDoneView, name="succes_post_addition")
]