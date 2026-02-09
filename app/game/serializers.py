from rest_framework import serializers
from game.models import PC, NPC, Spell, Session, Event, Item, Quest, Inventory, InventoryItem

class Spell(serializers.ModelSerializer):
    class Meta:
        model = Spell
        fields = ('id', 'title', 'description')

class PCSerializer(serializers.ModelSerializer):
    class Meta:
        model = PC
        fields = ('id', 'name', 'player', 'spells')

class NPCSerializer(serializers.ModelSerializer):
    class Meta:
        model = NPC
        fields = ('id', 'name', 'npc_type', 'dialogue')

class Session(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('id', 'player', 'start_time', 'end_time')

class Event(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'timestamp', 'event_type', 'session', 'details')

class Item(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'title', 'description')

class Quest(serializers.ModelSerializer):
    class Meta:
        model = Quest
        fields = ('id', 'title', 'event_trigger', 'description', 'status', 'reward')

class Inventory(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('id', 'player_c', 'created_at', 'updated_at')

class InventoryItem(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = ('id', 'inventory', 'item', 'quantity')
