from django.urls import path
from . import views

urlpatterns = [
    path('temp/', views.adminhome, name='adminhome'),
   
]