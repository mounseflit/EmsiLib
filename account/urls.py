from django.urls import  path
from . import views

LOGIN_URL = 'account/login'
urlpatterns = [
    path('signup/', views.register,name="register"),
    path('login/', views.connect,name="login"),
    path('infos/', views.infos,name="infos"),
    path('update/',views.update,name="update"),
    path('logout/',views.disconnect,name="logout"),

    ]









