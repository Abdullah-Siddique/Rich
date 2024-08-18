# checkup/urls.py
from django.urls import path
from .views import checkup

urlpatterns = [
    path('checkup/', checkup, name='checkup'),
]



