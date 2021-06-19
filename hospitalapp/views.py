from django.core.mail import message
from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Department,Doctor


def doctor_list(request,department_slug=None):
    department=None
    departments=Department.objects.all()
    doctors=Doctor.objects.all()
    if department_slug:
        department=get_object_or_404(Department,slug=department_slug)
        doctors=doctors.filter(department=department)
    return render(request,"index.html",{"departments":departments,"department":department,"doctors":doctors})


def doctor_detail(request,department_slug,slug):
    doctors = Doctor.objects.get(department__slug=department_slug, slug=slug)
    return render(request, "doctor_detail.html", {'doctors': doctors})








# def test(request):
#     return HttpResponse("hellooo")