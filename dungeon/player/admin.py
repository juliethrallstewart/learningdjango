from django.contrib import admin


# Register your models here.
from .models import Player, Item, Monster

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'location', 'experience', 'health')

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'slot', 'location', 'quality_points', 'stamina', 'strength', 'intelligence')

class MonsterAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'location', 'monster_type', 'experience_value')

admin.site.register(Player, PlayerAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Monster, MonsterAdmin)        