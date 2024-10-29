from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    cv = models.FileField(upload_to='cvs/', blank=True)
    
    def __str__(self):
        return f"Profil de {self.user.username}"
