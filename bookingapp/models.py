from datetime import datetime


from django import forms
from django.db import models

# Create your models here.


from hospitalapp.models import Department, Doctor


class BookingModel(models.Model):
    name=models.CharField(max_length=250)
    age=models.IntegerField()
    number=models.IntegerField()
    department=models.ForeignKey(Department,on_delete=models.SET_NULL,null=True)
    doctor=models.ForeignKey(Doctor,on_delete=models.SET_NULL,null=True)




