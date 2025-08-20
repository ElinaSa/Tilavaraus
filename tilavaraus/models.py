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

# Monta moneen taulut

class User(models.Model): # Varaajan tiedot
    user_id = models.IntegerField() # Varaajalle automaattisesti annettava juokseva numero
    first_name = models.CharField(max_length=50) # Varaajan etunimi
    last_name = models.CharField(max_length=50) # Varaajan sukunimi
    student_number = models.TextField(blank=True, null=True) # 5-numeroinen opiskelijanumero jos varaaja on opiskelija
    team = models.CharField(max_length=10) # Varaajan luokan/ryhmän tunnus, esim. Tivi-20oa   
    e_mail = models.CharField(max_length=50)# Varaajan sähköpostiosoite
    phone = models.TextField(blank=True, null=True) # Varaajan puhelinnumero
    # Foreign keyt, jotka linkitetty tauluun
    group = models.ForeignKey(UserGroup,on_delete=models.CASCADE)

def __str__(self):
    return self.user_id


class Reservation(models.Model):  # Varauksen tiedot
    reservation_id = models.IntegerField() # Varaukselle automaattisesti annettava juokseva numero
    reservation_date = models.DateField() # Varauksen päivä
    reservation_begins = models.TimeField() # Varauksen alkamisaika
    reservation_ends = models.TimeField() # Varauksen päättymisaika
    # Foreign keyt, jotka linkitetty tauluun
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.ForeignKey(Space,on_delete=models.CASCADE)
       
def __str__(self):
    return self.reservation_id