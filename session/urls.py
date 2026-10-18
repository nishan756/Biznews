from .views import user_login, user_logout, user_signup

from django.urls import path

urlpatterns = [
    path("signup/", user_signup, name = "signup"),

    path("login/", user_login, name = "login"),

    path("logout/", user_logout, name = "logout"),
    
]