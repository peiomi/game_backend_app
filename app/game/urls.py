from django.urls import path
from game import views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('api/spells/', views.spells_list, name='spell-list'),
    path('api/spells/<int:pk>/', views.spell_detail, name='spell-detail'),

    path('api/pcs/', views.pc_list, name='pc-list'),
    path('api/pcs/<int:pk>/', views.pc_detail, name='pc-detail'),

    path('api/npcs/', views.npc_list, name='npc-list'),
    path('api/npcs/<int:pk>/', views.npc_detail, name='npc-detail'),

    path('api/sessions/', views.session_list, name='session-list'),
    path('api/sessions/<int:pk>/', views.session_detail, name='session-detail'),

    path('api/events/', views.event_list, name='event-list'),
    path('api/events/<int:pk>/', views.event_detail, name='event-detail'),

    path('api/items/', views.item_list, name='item-list'),
    path('api/items/<int:pk>/', views.item_detail, name='item-detail'),

    path('api/quests/', views.quest_list, name='quest-list'),
    path('api/quests/<int:pk>/', views.quest_detail, name='quest-detail'),

    path('api/inventories/', views.inventory_list, name='inventory-list'),
    path('api/inventories/<int:pk>/', views.inventory_detail, name='inventory-detail'),

    path('api/inventory-items/', views.inventory_item_list, name='inventory-item-list'),
    path('api/inventory-items/<int:pk>/', views.inventory_item_detail, name='inventory-item-detail'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)