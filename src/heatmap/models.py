from django.db import models

# Create your models here.

class Collision(models.Model):
    date = models.CharField(max_length=120)
    latitude = models.CharField(max_length=120)
    longitude = models.CharField(max_length=120)
