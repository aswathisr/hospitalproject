from django import forms

from hospitalapp.models import Doctor
from .models import BookingModel


class BookingForm(forms.ModelForm):
    class Meta:
        model=BookingModel
        fields=["name","age","number","doctor",]
        labels={"name":"Name","age":"Age","number":"Mobile Number","doctor":"Doctor Name",}

