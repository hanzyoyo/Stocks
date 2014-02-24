from django.shortcuts import render

# Create your views here.

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

	return render(request, 'connexion.html',locals())
