from django.db import models


# Create your models here.
from django.urls import reverse


class Department(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug=models.SlugField(max_length=250,unique=True)


    class Meta:
        ordering = ('title',)
        verbose_name = 'department'
        verbose_name_plural = 'departments'

    def get_url(self):
        return reverse("hospitalapp:doctors_by_department", args=[self.slug])

    def __str__(self):
        return self.title



class Doctor(models.Model):
    department=models.ForeignKey(Department,related_name='doctors',on_delete=models.CASCADE)
    name=models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    details = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='doctors', blank=True)


    class Meta:
        ordering = ('name',)

    def get_url(self):
        return reverse("hospitalapp:doctor_detail",args=[self.department.slug,self.slug])


    def __str__(self):
        return self.name

