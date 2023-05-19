from django.urls import  path
from . import views


urlpatterns = [
    path('update/', views.register,name="account"),
    path('', views.connect,name="account"),

    ]









