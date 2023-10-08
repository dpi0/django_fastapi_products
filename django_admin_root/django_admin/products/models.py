from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    likes = models.PositiveIntegerField(default=0)


class User(models.Model):
    name = models.CharField(max_length=100, blank=True)
