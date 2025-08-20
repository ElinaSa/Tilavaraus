from django.contrib import admin
from .models import Space, UserGroup, User, Reservation

# Register your models here.
admin.site.register(Space)
admin.site.register(UserGroup)
admin.site.register(User)
admin.site.register(Reservation)