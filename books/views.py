from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404
from .models import Livre,Commentaire,Reservation



def search(request):

    if request.method=='POST' :
        searched=request.POST['searched']
        #livres = Livre.objects.filter(categorie__contains=searched)
        #livres = Livre.objects.filter(description__contains=searched)
        livres = Livre.objects.filter(nom__contains=searched)
        #livres = Livre.objects.filter(auteur__contains=searched)
        
        return render(request, 'search.html', {'searched' : searched,'livres' : livres})
    else :
        return render(request, 'search.html', {})



def index(request):
    livre_object = Livre.objects.all()
    return render(request, 'browse.html', {'livre_object': livre_object})


def detail(request, livre_id):
    livre = get_object_or_404(Livre, id=livre_id)
    commentaires = Commentaire.objects.filter(nomLivre=livre)
    date_debut = datetime.now().date()
    date_fin = date_debut + timedelta(days=30)
    if request.method == 'GET':
        context = {'livre': livre, 'commentaires': commentaires}
        return render(request, 'detailLivre.html', context)
    elif request.method == 'POST':
        contenu = request.POST.get("contenu")
        utilisateur = request.user

        if 'reserve_button' in request.POST:
            livre.etat = 'Réservé'  # Mettre à jour l'état du livre
            livre.save()
            Reservation.objects.create(reservateur=utilisateur, nomLivre=livre,DateDebut=date_debut,DateFin=date_fin)
            return redirect('detail', livre_id=livre_id)

        Commentaire.objects.create(nomLivre=livre, contenu=contenu, utilisateur=utilisateur)
        context = {'livre': livre, 'commentaires': commentaires}
        return render(request, 'detailLivre.html', context)

