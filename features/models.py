from django.db import models
from django.db.models.base import Model

# Create your models here.

class Info(models.Model):
    name = models.CharField(max_length=256)
    contact = models.IntegerField()
    interests = models.CharField(max_length=256)
    
