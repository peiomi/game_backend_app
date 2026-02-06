from django.db import models

# Create your models here.
class PC(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')