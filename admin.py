from django.contrib import admin
from .models import Food

# Register your models here.


@admin.register(Food)

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name' , 'description' , 'rate' , 'price')
    prepopulated_fields = {'slug' : ('name',)} #auto fill slug when writing food name