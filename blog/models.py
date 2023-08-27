from django.db import models
from datetime import datetime


# Create your models here.
class Deneyim(models.Model):
    title = models.CharField(max_length=100)
    title1 = models.CharField(max_length=120)
    title2 = models.TextField(max_length=2000)
    date = models.DateField(default=datetime.now)

class Okul(models.Model):
    title = models.CharField(max_length=100)
    title1 = models.CharField(max_length=120)
    title2 = models.TextField(max_length=2000)
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.title
