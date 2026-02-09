from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404 #render
# from django.http.response import JsonResponse
# from rest_framework.parsers import JSONParser
# from rest_framework.renderers import TemplateHTMLRenderer
# from rest_framework.views import APIView
from game.models import ( 
    PC, NPC, Spell, Session, Event, Item, Quest, Inventory, InventoryItem
)
from game.serializers import (
    PCSerializer, NPCSerializer, SpellSerializer, SessionSerializer,
    EventSerializer, ItemSerializer, QuestSerializer, InventorySerializer,
    InventoryItemSerializer
)
"""
The Django Docs explain how to use their generic views, which would 
make this code much cleaner, but I am writing my own functions to help 
me fully understand the concept of API.
"""


# spell views
@api_view(['GET', 'POST'])
def spell_list(request):
    if request.method == 'GET':
        spells = Spell.objects.all()
        serializer = SpellSerializer(spells, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SpellSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def spell_detail(request, pk):
    spell = get_object_or_404(Spell, pk=pk)
    if request.method == 'GET':
        serializer = SpellSerializer(spell)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = SpellSerializer(spell, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        spell.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# pc views
@api_view(['GET', 'POST'])
def pc_list(request):
    if request.method == 'GET':
        all_playable_characters = PC.objects.all()
        serializer = PCSerializer(all_playable_characters, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PCSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def pc_detail(request, pk):
    pc = get_object_or_404(PC, pk=pk)
    if request.method == 'GET':
        serializer = PCSerializer(pc)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PCSerializer(pc, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        pc.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# npc views
@api_view(['GET', 'POST'])
def npc_list(request):
    if request.method == 'GET':
        npcs = NPC.objects.all()
        serializer = NPCSerializer(npcs, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = NPCSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def npc_detail(request, pk):
    npc = get_object_or_404(NPC, pk=pk)
    if request.method == 'GET':
        serializer = NPCSerializer(npc)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = NPCSerializer(npc, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        npc.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# def index(request):
#     return render(request, "tutorials/index.html")

""" class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'tutorials/index.html'

    def get(self, request):
        queryset = Tutorial.objects.all()
        return Response({'tutorials': queryset}) """

