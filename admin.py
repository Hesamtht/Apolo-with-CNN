from django.contrib import admin
from .models import Reservation



# Register your models here.

@admin.register(Reservation)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ['name' , 'phone' , 'number_of_persons' , 'date']
    list_filter = ['number_of_persons']