from django.urls import  path
from .views import index, detail, search
from . import views

urlpatterns = [
    path('', views.index,name="books"),
    path('<int:livre_id>', views.detail,name="detail"),
    path('search', views.search,name="search")
    ]









