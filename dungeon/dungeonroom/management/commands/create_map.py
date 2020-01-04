from django.core.management.base import BaseCommand, CommandError
from dungeonroom.models import Room
from PIL import Image

class Command(BaseCommand):
    def handle(self, *args, **options):

        rooms = Room.objects.all()
        map = Image.new('RGB', (1200, 1200), color='white')
        room_image = Image.new('RGB', (50, 50), color='black')
        hallway_image_n = Image.new('RGB', (10, 10), color='red')
        hallway_image_s = Image.new('RGB', (10, 10), color='blue')
        hallway_image_e = Image.new('RGB', (10, 10), color='yellow')
        hallway_image_w = Image.new('RGB', (10, 10), color='green')

        for room in rooms:
            map.paste(room_image, (room.pos_x *60, room.pos_y *60))
            if room.connection_north is not None:
                map.paste(hallway_image_n, (room.pos_x *60+20, room.pos_y *60+50))
            # if room.connection_south is not None:
                map.paste(hallway_image_s, (room.pos_x *60+20, room.pos_y *60))
            if room.connection_east is not None:
                map.paste(hallway_image_e, (room.pos_x *60+50, room.pos_y *60+20))
            if room.connection_west is not None:
                map.paste(hallway_image_w, (room.pos_x *60, room.pos_y *60+20))
            #north
            #south
            #east
            #west
        map.save('blank_map.png')
 