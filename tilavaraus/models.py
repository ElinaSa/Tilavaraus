from django.db import models

# Create your models here.
# Luodaan kokeilua varten Reservation
class Reservation(models.Model):
    title = models.CharField(max_length=200)
    