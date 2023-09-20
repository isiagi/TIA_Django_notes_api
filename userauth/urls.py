from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name="Login User"),
    path('signup', views.signup, name="Signup User")
]