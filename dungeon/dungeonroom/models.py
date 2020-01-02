from django.db import models

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

    def __str__(self):
        return self.name

