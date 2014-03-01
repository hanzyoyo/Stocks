#-*- coding: utf-8 -*-

from django import forms
from evenement.models import Creneau

class IndexForm(forms.Form):
	heure = forms.ModelChoiceField(queryset=Creneau.objects.all())
	nb_kebabs = forms.ChoiceField(widget=forms.Select, choices=('1','2','3'))
