from django.contrib import admin
from .models import Space, UserGroup, Person, Reservations
# 
# Register your models here.
admin.site.register(Space)
admin.site.register(UserGroup) 
admin.site.register(Person)
admin.site.register(Reservations)

