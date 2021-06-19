from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import BookingModel

@admin.register(BookingModel)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BookingModel._meta.get_fields()]
