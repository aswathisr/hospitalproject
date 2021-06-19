from django.contrib import messages
from django.http import JsonResponse

from django.shortcuts import render

# Create your views here.
from hospitalapp.models import Doctor
from .forms import BookingForm
from .models import BookingModel


def BookingView(request):
    if request.method == "POST":
        form = BookingForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,
                             "Request for Appoinment is created and wait for confirmation message from hospital")
    else:
        form = BookingForm()

    return render(request, 'bookingform.html', {"bookform": form})



