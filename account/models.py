from django.db import models
#from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(models.Model):
        nomComplet= models.CharField(max_length=100, unique=True)
        groupe= models.CharField(max_length=100)
        email= models.EmailField(unique=True)
        password= models.CharField(max_length=100)

        def __str__(self):
           return str(self.nomComplet)