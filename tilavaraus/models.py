from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Yksi moneen taulut

class Space(models.Model): # Varattavat tilat
    room = models.CharField(max_length=50) # Varattavissa oleva numeroitu huone
    address = models.CharField(max_length=50) # Huoneen osoite
    location = models.TextField(blank=True, null=True) # Huoneen tarkempi sijainti

def __str__(self):
    return self.room      
 

class UserGroup(models.Model): # Käyttäjäryhmä, kuten opiskelijat, opettajat, muu henkilökunta tms.
    group =models.CharField(max_length=50) # Käyttäjäryhmä jolle määritelty tietyt oikeudet
    rights = models.CharField(max_length=200) # Ryhmälle määritellyt oikeudet

def __str__(self):
    return self.group 
























