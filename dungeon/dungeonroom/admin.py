from django.contrib import admin

# Register your models here.
from .models import Room, Floor
# This is setting up exactly what will display in the dashboard (ie: what fields)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'floor', 'pos_x', 'pos_y', 'connections')

class FloorAdmin(admin.ModelAdmin):
    list_display  = ('name', 'level', 'num_rooms')


admin.site.register(Room, RoomAdmin)
admin.site.register(Floor, FloorAdmin)