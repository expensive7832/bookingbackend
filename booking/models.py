from django.db import models

# Create your models here.

class Department(models.Model):
    title = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add = True)
    choosen_time = models.DateTimeField()
    dpt = models.ForeignKey(Department, on_delete=models.RESTRICT)
    reference =  models.CharField(max_length=50, null=True, blank=True)
    
