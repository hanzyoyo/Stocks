#coding=utf-8

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from evenement.models import Commande

@login_required
def paps(request):
    #creer l'objet commande a partir du call AJAX du formulaire

    client = request.user
    commande = Commande(creneau, client, nb_kebabs)
    commande.save()

    return render('evenement/confirmation.html', {'commande' : commande})

