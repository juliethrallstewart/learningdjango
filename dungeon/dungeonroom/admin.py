from django.contrib import admin

# Register your models here.
from .models import Room, Floor

class RoomAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'floor')

class FloorAdmin(admin.ModelAdmin):
    fields = ('name', 'level', 'num_rooms')


admin.site.register(Room, RoomAdmin)
admin.site.register(Floor)