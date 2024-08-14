from django.urls import path
from . import views

urlpatterns = [
    path('richest/', views.richest_people, name='richest_people'),
]
