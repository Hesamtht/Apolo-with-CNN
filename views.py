from django.shortcuts import render, redirect
from .models import Reservation  # Make sure to import the Reservation model


def reservation_success(request):

    return render(request , 'success.html')



def reserve_table(request):

    if request.method == 'POST':

        reservation = Reservation(
            name = request.POST.get('fullname'),
            phone = request.POST.get('phone'),
            email = request.POST.get('email'),
            date = request.POST.get('date'),
            time = request.POST.get('time'),
            number_of_persons = request.POST.get('guests'),
        )

        reservation.save()

        return redirect('reservation:reservation_success')

    else:


        return render(request , 'reservation.html')
