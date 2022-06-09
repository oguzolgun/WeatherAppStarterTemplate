from django.urls import path
from .views import delete_city, home

urlpatterns = [
    path('', home, name="home"),
    path('delete/<int:id>', delete_city, name="delete"),
]