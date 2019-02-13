from django.urls import path
from .import views

urlpatterns = [
    path('Mentor', views.Mentor, name='Mentor'),
]