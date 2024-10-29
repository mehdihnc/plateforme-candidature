from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class JobOffer(models.Model):
    """
    Modèle représentant une offre d'emploi.
    Les offres sont créées par les super_users via l'interface d'administration.
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

class Application(models.Model):
    """
    Modèle représentant une candidature.
    Lie un utilisateur à une offre d'emploi avec une lettre de motivation.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(JobOffer, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)
    cover_letter = models.TextField()
    
    class Meta:
        unique_together = ('user', 'job')
    
    def __str__(self):
        return f"{self.user.username} - {self.job.title}"
