from . import views
from django.urls import include,path
urlpatterns = [
    # path('',home ,name="home"),
    # path('success-page/' ,success_page ,name="success_page"),
    path('', views.navbarAdmin, name= 'navbarAdmin'),
   
]
