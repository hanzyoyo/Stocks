#-*- coding: utf-8 -*-

from django import forms

#définit le formulaire de connexion
class ConnectionForm(forms.Form):
	username = forms.CharField(max_length = 30)
	password = forms.CharField(widget=forms.PasswordInput)
	email = forms.EmailField();
