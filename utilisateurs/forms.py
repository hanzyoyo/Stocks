#config=utf-8

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#définition du formulaire d'inscription
class UserCreateForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit = True):
		user = super(UserCreateForm, self).save(commit=False)
		user.email = self.cleaned_data["email"]
		if commit:
			user.save()
		return user


#définition du formulaire de connexion
class ConnexionForm(forms.Form):
	username = forms.CharField(max_length = 30)
	password = forms.CharField(widget=forms.PasswordInput)
	email = forms.EmailField();
