from django.contrib import admin
from .models import Livre, Reservation, Emprunt, Commentaire

# Register your models here.
admin.site.register(Livre)
admin.site.register(Reservation)
admin.site.register(Emprunt)
admin.site.register(Commentaire)
