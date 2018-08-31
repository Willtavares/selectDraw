from django.db import models

# Create your models here.
class Coordinates(models.Model):
    
    dados = models.CharField(_(""), max_length=200)

    def __str__(self):
        return 

    def __unicode__(self):
        return 

