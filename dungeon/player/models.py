from django.db import models
from dungeonroom.models import Room

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    player_level = models.PositiveIntegerField()
    experience = models.PositiveIntegerField()
    health = models.PositiveIntegerField(default=10)
    mana_points = models.PositiveIntegerField(default=5)
    stamina = models.PositiveIntegerField(default=1)
    strength = models.PositiveIntegerField(default=1)
    intelligence = models.PositiveIntegerField(default=1)
    location = models.ForeignKey('dungeonroom.Room', on_delete=models.PROTECT)
    helmet = models.ForeignKey('Item', on_delete=models.PROTECT, null=True, blank=True, related_name='item_helmet')
    chest = models.ForeignKey('Item', on_delete=models.PROTECT, null=True, blank=True, related_name='item_chest')
    waist = models.ForeignKey('Item', on_delete=models.PROTECT, null=True, blank=True, related_name='item_waist')
    pants = models.ForeignKey('Item', on_delete=models.PROTECT, null=True, blank=True, related_name='item_pants')
    boots = models.ForeignKey('Item', on_delete=models.PROTECT, null=True, blank=True, related_name='item_boots')
    weapon = models.ForeignKey('Item', on_delete=models.PROTECT, null=True, blank=True, related_name='item_weapon')

    # def equip(self):
    #     HELMET = 'helmet'
    #     CHEST = 'chest'
    #     WAIST = 'waist'
    #     PANTS = 'pants'
    #     BOOTS = 'boots'
    #     WEAPON = 'weapon'

    #     # Take off old item
    #     if item.slot = HELMET:
    #         old_helmet = self.helmet

    #     # put on new item


    def __str__(self):
            return self.name

class Item(models.Model):
    ITEM_SLOTS = [('helmet', 'Helmet'), ('chest', 'Chest'), ('waist', 'Waist'), ('pants', 'Pants'), ('boots', 'Boots'), ('weapon', 'Weapon')]
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    stamina = models.PositiveIntegerField(default=0)
    strength = models.PositiveIntegerField(default=0)
    intelligence = models.PositiveIntegerField(default=0)
    slot = models.CharField(max_length=10, choices=ITEM_SLOTS)

    def create(cls, pos_x, pos_y):
 
    def __str__(self):
        return self.name