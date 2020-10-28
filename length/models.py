from django.db import models

# Create your models here.



class Measurement(models.Model):
    val = models.FloatField()
    unit_1 = models.CharField(max_length=3)
    unit_2 = models.CharField(max_length=3)