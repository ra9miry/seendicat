from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path("sign-up/", views.signUp, name="signUp"),
    path("login/", views.loginPage, name="loginPage"),
    path("logout/", views.logoutUser, name="logoutUser"),
]