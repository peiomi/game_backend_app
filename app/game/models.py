from django.db import models
from django.utils import timezone


class Spell(models.Model):
    title = models.CharField(max_length=50, blank=False, default='')
    description = models.TextField()

class PC(models.Model):
    name = models.CharField(max_length=50, blank=False, default='')
    player = models.ForeignKey('players.Player', on_delete=models.CASCADE, default='')
    spells = models.ManyToManyField(Spell)

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

class Item(models.Model):
    title = models.CharField(max_length=50, blank=False, default='')
    description = models.TextField()

class Quest(models.Model):
    status_choices = [
        ('available', 'Available'), 
        ('in_progress', 'In Progress'), 
        ('completed', 'Completed'), 
        ('failed', 'Failed')
        ]

    title = models.CharField(max_length=50, blank=False, default='')
    event_trigger = models.ForeignKey(Event, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=status_choices, blank=False, default='available')
    reward = models.ForeignKey(Item, on_delete=models.CASCADE)

class Inventory(models.Model):
    player = models.OneToOneField('players.Player', on_delete=models.CASCADE, related_name='inventory')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.player.username}'s Inventory"
    
class InventoryItem(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
