from django.db import models
from django.utils import timezone

# Create your models here.
class PC(models.Model):
    name = models.CharField(max_length=50, blank=False, default='')

class NPC(models.Model):
    name = models.CharField(max_length=50, blank=False, default='')
    npc_type = models.CharField(max_length=50, blank=False, default='')
    dialouge = models.TextField()

class Session(models.Model):
    player = models.ForeignKey('players.Player', on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)

class Event(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    event_type = models.CharField(max_length=50, blank=False, default='')
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    details = models.TextField()

