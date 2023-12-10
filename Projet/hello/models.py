from django.db import models
from django.utils import timezone
    
class Invite(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    presence_confirme = models.BooleanField(default=False)
    preferences_alimentaires = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.nom} {self.prenom}"
