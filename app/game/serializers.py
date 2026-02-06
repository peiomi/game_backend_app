from rest_framework import serializers
from game.models import PC, NPC


class PCSerializer(serializers.ModelSerializer):
    class Meta:
        model = PC
        fields = ('id', 'name')

class NPCSerializer(serializers.ModelSerializer):
    class Meta:
        model = NPC
        fields = ('id', 'name', 'npc_type', 'dialouge')
