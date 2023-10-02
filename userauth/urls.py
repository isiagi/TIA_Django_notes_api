from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name="login"),
    path('signup', views.signup, name="register"),
    path('logout', views.logout, name="logout"),
    path('forgot_password', views.forgot_password, name="Forgot Password Request"),
    path('reset-password/<str:encoded_pk>/<str:token>/', views.reset, name="reset-password"),
]