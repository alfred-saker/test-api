from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.CharField(max_length=100)
    paswword1 = models.CharField(max_length=100)
    paswword2 = models.CharField(max_length=100)
    # ... ajoutez d'autres champs requis
