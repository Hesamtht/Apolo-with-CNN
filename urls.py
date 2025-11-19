from django.urls import path
from .views import *

app_name = 'reservation'

urlpatterns = [
    path('' , reserve_table , name = 'reserve_table'),
    path('success/' , reservation_success , name = 'reservation_success'),
]