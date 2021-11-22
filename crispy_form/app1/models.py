from django.db import models

# Create your models here.
class Product(models.Model):
    company = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    price = models.FloatField()
    quantity = models.IntegerField()
    paid = models.BooleanField()
    city = models.CharField(max_length=32)
