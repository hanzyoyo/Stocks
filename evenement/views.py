#coding=utf-8

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from evenement.models import Commande, Evenement, Creneau
from evenement.forms import IndexForm

from django.utils import timezone

@login_required
def paps(request):
    #creer l'objet commande a partir du call AJAX du formulaire

    client = request.user
    commande = Commande(creneau, client, nb_kebabs)
    commande.save()

    return render(request,'evenement/confirmation.html', {'commande' : commande})

@login_required
def index(request):
	evenements = Evenement.objects.all().order_by('-date_evenement')

	if not evenements.count():
		return render(request, 'evenement/rien.html')
	else:
		evenement = evenements[0]

	if timezone.now() < evenement.date_paps :
		return render(request, 'evenement/rien.html')
	else:
		creneaux = Creneau.objects.filter(evenement = evenement)

	if request.method == 'POST':
		form = IndexForm(request.POST)
		if form.is_valid():
			nb_kebabs = form.cleaned_data["nb_kebabs"]
			creneau = form.cleaned_data["creneau"]

			#creneau = creneaux.filter(heure = heure)

			return redirect(paps,locals())
	else:
		form = IndexForm(creneaux)

	return render(request,'evenement/index.html',locals())
