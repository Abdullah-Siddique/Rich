from django.urls import path
from .views import checkup_view

urlpatterns = [
    path('checkup/', checkup_view, name='checkup'),
]


