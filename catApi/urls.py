from django.urls import path
from .views import random_cat
from .views import home

urlpatterns = [
    path('random/', random_cat, name='random_cat'),
    path('random/<int:count>/', random_cat, name='random_cats'),
    path('', home, name='home'),
]