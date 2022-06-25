from django.db import models

# Create your models here.
class Indiinfo(models.Model):
    email = models.EmailField()
    indivisual_ID = models.IntegerField()
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=9)
    status = models.BooleanField()
    store_ID = models.IntegerField()
