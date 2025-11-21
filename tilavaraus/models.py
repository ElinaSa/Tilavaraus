from django.db import models
from django.contrib.auth.models import User
# 
# Create your models here.

# Yksi moneen taulut

class Space(models.Model): # Varattavat tilat
    room = models.CharField(max_length=50, primary_key=True) # Varattavissa oleva numeroitu huone
    address = models.CharField(max_length=50) # Huoneen osoite
    location = models.TextField(blank=True, null=True) # Huoneen tarkempi sijainti

def __str__(self):
    return self.room
      
class UserGroup(models.Model): # Käyttäjäryhmä, kuten opiskelijat, opettajat, muu henkilökunta tms.
    group = models.CharField(max_length=50, primary_key=True) # Käyttäjäryhmä jolle määritelty tietyt oikeudet
    rights = models.CharField(max_length=200) # Ryhmälle määritellyt oikeudet

def __str__(self):
    return self.group 
 
# Monta moneen taulut

class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    group = models.ForeignKey(UserGroup, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_number = models.CharField(max_length=5)
    team = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.person_id} {self.first_name} {self.last_name}"
    
class Reservations(models.Model):
    reservation_id = models.AutoField(primary_key=True)

    room = models.ForeignKey(Space, on_delete=models.CASCADE)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)

    reservation_date = models.DateField()
    reservation_begins = models.TimeField()
    reservation_ends = models.TimeField()
   
    def __str__(self):
        return f"{self.reservation_id} {self.room} {self.person_id}"


















