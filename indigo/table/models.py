from django.db import models
from django.urls import reverse

# Create your models here.
class Company(models.Model):
    rank = models.IntegerField(unique=True)
    employer = models.CharField(max_length=100, unique=True)
    employeesCount = models.IntegerField()
    medianSalary = models.IntegerField()

    def get_absolute_url(self):
        return reverse('index')

    def __str__(self):
        return self.employer
