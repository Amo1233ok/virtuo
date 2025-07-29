from django.db import models

# Create your models here.
class Requete(models.Model):
    Nom = models.CharField(max_length=50)
    telephone = models.CharField(max_length=13)
    email = models.EmailField()
    objet = models.CharField(max_length=100)
    message = models.CharField(max_length=500)