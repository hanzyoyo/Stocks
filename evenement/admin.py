from django.contrib import admin
from evenement.models import Evenement,Creneau,Commande

# Register your models here for administration.
admin.site.register(Evenement)
admin.site.register(Creneau)
admin.site.register(Commande)
