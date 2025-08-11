from django.shortcuts import render

# Create your views here.


def user_sub(request):

    return render (request , 'subscription.html')