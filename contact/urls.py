from .views import contact

from django.urls import path

urlpatterns = [
    path("", contact, name = "contact"),
]