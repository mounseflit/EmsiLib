from django.urls import path
from .import views
#from django.contrib.auth

urlpatterns= [
    path('',views.Home.as_view(),name='home'),
]