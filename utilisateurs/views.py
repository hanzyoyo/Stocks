#coding=utf-8

from django.shortcuts import render,render_to_response
from evenement.forms import ConnexionForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.template import RequestContext

#vue pour la création d'un nouvel utilisateur
def registration(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
	else:
		form = UserCreationForm()
	
	return render_to_response('utilisateurs/registration.html', {'form': form,},context_instance=RequestContext(request))

#vue appelée pour la connexion d'un utilisateur
def connexion(request):
	error = False

	if request.method == "POST":
		form = ConnexionForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]  # Nous récupérons le nom d'utilisateur
			password = form.cleaned_data["password"]  # … et le mot de passe
			user = authenticate(username=username, password=password)  #Nous vérifions si les données sont correctes
			if user:  # Si l'objet renvoyé n'est pas None
				login(request, user)  # nous connectons l'utilisateur
			else: #sinon une erreur sera affichée
				error = True
	else:
		form = ConnexionForm()

	return render(request, 'utilisateurs/connexion.html',locals())
