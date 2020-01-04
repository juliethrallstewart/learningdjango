from django.contrib import admin

# Register your models here.
from .models import Player

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'location', 'score', 'inventory')