from django.db import models

class Reservation(models.Model):

    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    phone = models.CharField(max_length = 11)
    number_of_persons = models.PositiveIntegerField()
    time = models.TimeField()
    date = models.DateField()


    def __str__(self):
        return self.name
