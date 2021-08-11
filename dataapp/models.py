from django.db import models

# Create your models here.

class PharmaSales(models.Model):
    year = models.CharField(max_length=255)
    datum = models.DateTimeField(auto_now_add=True)
    m01ab = models.CharField(max_length=255)
    m01ae = models.CharField(max_length=255)
    n02ba = models.CharField(max_length=255)
    n02be = models.CharField(max_length=255)
    n05b = models.CharField(max_length=255)
    n05c = models.CharField(max_length=255)
    r03 = models.CharField(max_length=255)
    r06 = models.CharField(max_length=255)
