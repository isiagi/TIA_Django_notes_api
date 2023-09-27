from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name="Login User"),
    path('signup', views.signup, name="Signup User"),
    path('logout', views.logout, name="Logout User"),
    path('forgot_password', views.forgot_password, name="Forgot Password Request"),
    path('reset-password/<str:encoded_pk>/<str:token>/', views.reset, name="reset-password"),
]