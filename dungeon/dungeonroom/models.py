from django.db import models
# from player.models import Item
import random

# Create your models here.
class Floor(models.Model):
    name = models.CharField(max_length=200)
    level = models.PositiveIntegerField()
    num_rooms = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    floor = models.ForeignKey('Floor', on_delete=models.CASCADE)
    pos_x = models.PositiveIntegerField()
    pos_y = models.PositiveIntegerField()
    connections = models.PositiveIntegerField(default=0)
    connection_north = models.ForeignKey('Room', on_delete=models.CASCADE, null=True, blank=True, related_name='room_north')
    connection_south = models.ForeignKey('Room', on_delete=models.CASCADE, null=True, blank=True, related_name='room_south')
    connection_east = models.ForeignKey('Room', on_delete=models.CASCADE, null=True, blank=True, related_name='room_east')
    connection_west = models.ForeignKey('Room', on_delete=models.CASCADE, null=True, blank=True, related_name='room_west')

    def connected(self, room):
        if room in [self.connection_north, self.connection_south, self.connection_east, self.connection_west]:
            return True
        return False

    def __str__(self):
        return self.name

