#coding=utf-8

from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

# Create your models here.

class Evenement(models.Model):
	#constantes
	duree_creneau = 15

	date_paps = models.DateTimeField(u'Date du paps')
	date_evenement = models.DateTimeField(u'Date de l\'événement')
	total_kebabs = models.IntegerField(max_length = 3)
	kebabs_par_creneaux = models.IntegerField(max_length = 2)

	#override de l'affichage dans l'interface admin
	class Meta:
		verbose_name = u'Événement'
		verbose_name_plural = u'Événements'
		get_latest_by = u'date_evenement'


class Creneau(models.Model):
	evenement = models.ForeignKey(Evenement)
	kebab_restant = models.IntegerField(u'nombre de kebabs encore papsables sur ce créneau', max_length=2)
	heure = models.DateTimeField(u'heure à laquelle il faut apporter la commande')

	def __unicode__(self):
		return unicode(self.heure)

	class Meta:
		verbose_name = 'Créneau'
		verbose_name_plural = 'Créneaux'
        ordering = ['heure']

class Commande(models.Model):
	creneau = models.ForeignKey(Creneau)
    #TODO : client = models.ForeignKey('Client')
	commande = models.IntegerField(u'Nombre de kebabs commandés')

	def delete(self, *args, **kwargs):
		#On rajoute les places au créneau
		self.creneau.kebab_restant += self.commande
		self.creneau.save()

		super(Commande, self).delete(*args, **kwargs)

    #TODO : definir le save pour retirer les kebabs du creneau une fois la commande validee par mail

	def save(self, *args, **kwargs):
		self.creneau.kebab_restant -= self.commande
		self.creneau.save()

		super(Commande, self).save(*args, **kwargs)
