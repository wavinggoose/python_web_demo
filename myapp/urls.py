from django.urls import path

from . import views

urlpatterns = [
    path('pa', views.pa),
]