from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('userpage/', views.userPerson, name='userpage'),
    path('logout/', views.custom_logout, name='custom_logout'),
    
]