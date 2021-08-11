from django.db import models
import uuid


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
    def __str__(self):
        return (str(self.id))

class DrugsReview(models.Model):
    # unique_id = models.AutoField(primary_key=False)
    condition = models.CharField(max_length=255, default="")
    date = models.DateField(null=True)
    drug_name = models.CharField(max_length=255, default="")
    rating = models.CharField(max_length=255, default="")
    review = models.CharField(max_length=255, default="")
    useful_count = models.CharField(max_length=255, default="")
    year = models.CharField(max_length=255, default="")
