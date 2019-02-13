from django.urls import path
from .import views

urlpatterns = [
    path('Mentee', views.Mentee, name='Mentee'),
]