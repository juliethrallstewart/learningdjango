from django.contrib import admin

# Register your models here.
from .models import Room, Floor
from player.models import Player, Item, Monster
# This is setting up exactly what will display in the dashboard (ie: what fields)
class ItemInline(admin.TabularInline):
    model = Item

class PlayerInline(admin.TabularInline):
    model = Player

class MonsterInline(admin.TabularInline):
    model = Monster

class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'floor', 'pos_x', 'pos_y', 'connections')

    inlines = [ItemInline, PlayerInline, MonsterInline]

class FloorAdmin(admin.ModelAdmin):
    list_display  = ('name', 'level', 'num_rooms')


admin.site.register(Room, RoomAdmin)
admin.site.register(Floor, FloorAdmin)
