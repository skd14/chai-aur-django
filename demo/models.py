from django.db import models
from django.utils import timezone

# Create your models here.
class EmployeeDetails(models.Model):
    DOMAIN = [
        ('IT', 'INFORMATION TECHNOLOGY'),
        ('NON IT', 'NON INFORMATION TECHNOLOGY')
    ]
    employee_id = models.IntegerField(null=True, blank=True, unique=True)
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    field = models.CharField(max_length=8, choices=DOMAIN)
    image = models.ImageField(upload_to='demo_proj/')

    def __str__(self):
        return self.name