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
    return f"{self.room}"
      
# class UserGroup(models.Model): # Käyttäjäryhmä, kuten opiskelijat, opettajat, muu henkilökunta tms.
    # group = models.CharField(max_length=50, primary_key=True) # Käyttäjäryhmä jolle määritelty tietyt oikeudet
    # rights = models.CharField(max_length=200) # Ryhmälle määritellyt oikeudet
# 
# def __str__(self):
    # return self.group 
 
# Monta moneen taulut

# class Person(models.Model):
    # email = models.AutoField(primary_key=True)
    # group = models.ForeignKey(UserGroup, on_delete=models.CASCADE)
# 
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    # team = models.CharField(max_length=10)
    # phone = models.CharField(max_length=20)
# 
    # def __str__(self):
        # return f"{self.email} {self.first_name} {self.last_name}"
    # 
class Booking(models.Model):
    bookingID = models.AutoField(primary_key=True)

    room = models.ForeignKey(Space, on_delete=models.CASCADE)
    email = models.ForeignKey(User, on_delete=models.CASCADE)

    date = models.DateField()
    begins = models.TimeField()
    ends = models.TimeField()
   
    def __str__(self):
        return f"{self.bookingID} {self.room} {self.date} {self.begins} {self.ends}"


















