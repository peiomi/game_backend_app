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





# def index(request):
#     return render(request, "tutorials/index.html")

""" class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'tutorials/index.html'

    def get(self, request):
        queryset = Tutorial.objects.all()
        return Response({'tutorials': queryset}) """



@api_view(['GET', 'POST', 'DELETE'])
def inventory_list(request):
    if request.method == 'GET':
        inventory = Inventory.objects.all()

        player_c = request.GET.get('player_c', None)
        if player_c is not None:
            inventory = inventory.filter(player_c__icontains=player_c)

        inventory_serializer = InventorySerializer(inventory, many=True)
        return JsonResponse(inventory_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        inventory_data = JSONParser().parse(request)
        inventory_serializer = InventorySerializer(data=inventory_data)
        if inventory_serializer.is_valid():
            inventory_serializer.save()
            return JsonResponse(inventory_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(inventory_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Inventory.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} Inventory were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    try:
        tutorial = Tutorial.objects.get(pk=pk)
    except Tutorial.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        tutorial_serializer = TutorialSerializer(tutorial)
        return JsonResponse(tutorial_serializer.data)

    elif request.method == 'PUT':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(tutorial, data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data)
        return JsonResponse(tutorial_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tutorial.delete()
        return JsonResponse({'message': 'Tutorial was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def tutorial_list_published(request):
    tutorials = Tutorial.objects.filter(published=True)

    if request.method == 'GET':
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)