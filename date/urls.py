from django.urls import path
from . import views
urlpatterns = [
    path('date/', views.date_view, name='date_view'),
]
