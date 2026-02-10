import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from players.models import Player
from game.models import ( 
    PC, NPC, Spell, Session, Event, Item, Quest, Inventory, InventoryItem
)
from game.serializers import (
    PCSerializer, NPCSerializer, SpellSerializer, SessionSerializer,
    EventSerializer, ItemSerializer, QuestSerializer, InventorySerializer,
    InventoryItemSerializer
)

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_spell_model():
    s = Spell.objects.create(title="Sunball", description="Burns")
    assert s.pk is not None
    assert s.title == "Sunball"
    assert "Burns" in s.description

@pytest.mark.django_db
def test_pc_and_spells():
    player = Player.objects.create_user(username="tester", password='password123')
    pc = PC.objects.create(name="Herc", player=player)
    spell = Spell.objects.create(title='Heal', description='Restore HP')
    pc.spells.add(spell)
    pc.refresh_from_db()
    assert pc.spells.count() == 1
    assert pc.spells.first().title == 'Heal'

@pytest.mark.django_db
def test_inventory_and_items():
    player = Player.objects.create_user(username="gamergirl", password="123456789")
    pc = PC.objects.create(name="Meg", player=player)
    inventory = Inventory.objects.create(player_c=pc)
    item = Item.objects.create(title="Idol", description="Teleports")
    item2 = Item.objects.create(title="Potion", description="Poison")

    InventoryItem.objects.create(inventory=inventory, item=item, quantity=1)
    InventoryItem.objects.create(inventory=inventory, item=item2, quantity=2)

    with pytest.raises(Exception):
        InventoryItem.objects.create(inventory=inventory, item=item, quantity=2)


@pytest.mark.django_db
def test_spell_serializer():
    s = Spell.objects.create(title="SnowFart", description="Cold and Smelly")
    serialized = SpellSerializer(s)
    assert serialized.data["title"] == "SnowFart"
    assert "description" in serialized.data

@pytest.mark.django_db
def test_spell_list_api(api_client):
    url = reverse("spell-list")
    get_response = api_client.get(url)
    post_response = api_client.post(url, {"title": "Laser", "description": "Beam"}, format="json")
    assert get_response.status_code == status.HTTP_200_OK
    assert post_response.status_code == status.HTTP_201_CREATED
    assert post_response.data["title"] == "Llama"

@pytest.mark.django_db
def test_spell_detail_api(api_client):
    s = Spell.objects.create(title="Cosmic Rain", description="Rain that is cosmic")
    url = reverse("spell-detail", args=[s.pk])
    get_response = api_client.get(url)
    put_response = api_client.put(url, {"title": "Rain Cosmic", "description": "Cosmic that is Rain"}, format="json")
    delete_response = api_client.delete(url)
    assert get_response.status_code == status.HTTP_200_OK
    assert put_response.status_code == status.HTTP_200_OK
    assert put_response.data["title"] == "Rain Cosmic"
    assert delete_response.status_code == status.HTTP_204_NO_CONTENT