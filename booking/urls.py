from django.urls import path
from .views import getDepartment, InsertAppointment

urlpatterns = [
    path("getdepartment/", getDepartment ),
    path("appointment/", InsertAppointment)
]