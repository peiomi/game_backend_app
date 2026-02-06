from django.db import models

# Create your models here.
class PC(models.Model):
    name = models.CharField(max_length=50, blank=False, default='')

class NPC(models.Model):
    name = models.CharField(max_length=50, blank=False, default='')
    npc_type = models.CharField(max_length=50, blank=False, default='')
    dialouge = models.TextField()

