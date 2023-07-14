from django.db import models
from account.models import User
from datetime import datetime, timedelta

class Livre(models.Model):
    # Fields here
    objects = models.Manager()

# Create your models here.
class Livre(models.Model):
        Categorie=(("Informatique","Informatique"),("Automatisme","Automatisme"),("Industriel","Industriel"))
        Etat=(("Disponible","Disponible"),("Réservé","Réservé"),("Emprunté","Emprunté"))
        Rate=((1,1),(2,2),(3,3),(4,4),(5,5))
        nom= models.CharField(max_length=100)
        auteur= models.CharField(max_length=100)
        categorie= models.CharField(max_length=100, choices= Categorie)
        etat= models.CharField(max_length=100, choices= Etat)
        rate= models.IntegerField(choices= Rate, null= True)
        description= models.CharField(max_length=300, null= True)
        image=models.CharField(max_length=5000)
 
        
        def __str__(self):
           return str(self.nom)
        
class Reservation(models.Model):
        reservateur=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
        nomLivre=models.ForeignKey(Livre, on_delete=models.CASCADE, null=True)
        DateDebut= models.DateField(default=datetime.now)
        DateFin= models.DateField(null=True, blank=True)

        def __str__(self):
           return str(self.nomLivre) + " reservé par " + str(self.reservateur)


class Emprunt(models.Model):
        emprunteur=models.ForeignKey(User, on_delete=models.PROTECT, null=True)
        nomLivre= models.ForeignKey(Livre, on_delete=models.PROTECT, null=True)
        DateDebut= models.DateField(default=datetime.now)
        DateFin= models.DateField(null=True, blank=True)

        def __str__(self):
           return str(self.nomLivre) + " Emprunté par " + str(self.emprunteur)

class Commentaire(models.Model):
        utilisateur=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
        nomLivre= models.ForeignKey(Livre, on_delete=models.CASCADE, null=True)
        contenu= models.CharField(null=True, max_length=100)

        def __str__(self):
           return str(self.nomLivre) + " commenté par " + str(self.utilisateur)
        

        