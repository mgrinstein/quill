from django.db import models

# Create your models here.

class Repository(models.Model):
    path = models.CharField(max_length=200)