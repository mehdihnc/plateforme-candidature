from django.contrib.auth.models import User
from django.db import models

class ProfilCandidat(models.Model):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)
    cv = models.FileField(upload_to='cvs/', blank=True, null=True)

    def __str__(self):
        return f"{self.utilisateur.username} - Profil"
