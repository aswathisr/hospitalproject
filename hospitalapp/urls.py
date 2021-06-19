"""hospitalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views
app_name='hospitalapp'

urlpatterns = [
    path('',views.doctor_list,name="doctors_list"),
    path("<slug:department_slug>/",views.doctor_list,name="doctors_by_department"),
    path('<slug:department_slug>/<slug:slug>/', views.doctor_detail, name='doctor_detail'),

    # path("",views.test,name="test"),
]
