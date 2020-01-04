from django.core.management.base import BaseCommand, CommandError
from dungeonroom.models import Floor, Room
import random
import pickle

random.seed(5)

room_descriptions = pickle.load(open('../room_descriptions.p', 'rb'))

room_names = ['Amphitheater',
'Antechamber',
'Asylum',
'Atrium',
'Battlement',
'Belfry',
'Cave',
'Cavern',
'Chapel',
'Cloister',
'Coliseum',
'Courtyard',
'Depository',
'Foyer',
'Gallery',
'Garden',
'Garderobe',
'Greenhouse',
'Hideaway',
'Hold',
'Infirmary',
'Keep',
'Kitchen',
'Laboratory',
'Labrynth',
'Library',
'Minaret',
'Mine',
'Necropolis',
'Nursery',
'Observatory',
'Office',
'Ossuary',
'Oubliette',
'Pantry',
'Park',
'Passageway',
'Prison',
'Rampart',
'Repository',
'Room',
'Sanctum',
'Sepulcher',
'Spire',
'Stairwell',
'Steeple',
'Storage Room',
'Study',
'Sunroom',
'Temple',
'Threshold',
'Tower',
'Tunnel',
'Turret',
'Vault',
'Vestibule',
'Walkway',
'Dormitory',
'Eating hall',
'Master bedroom',
'Storeroom',
'Forge',
'Bath',
'Summoning room',
'Jail',
'Shrine',
'Courthall',
'Armory',
'Latrine',
'Guard post',
'Throne Room',
'Barracks',
'Pool/Well',
'Pantry/Storage',
'Wine Cellar',
'Meditation Room',
'Privy',
'Ballroom',
'Great Hall',
'Training Hall',
'Trophy Hall',
'Propylaeum',
'Conservatory',
'Kennel',
'Larder',
'Crematorium',
'Panopticon',
'Tomb',
'Crypt',
'Workshop',
'Foundry',
'Meeting Hall',
'Parlor',
'Sitting Room',
'Anteroom',
'Entrance Hall',
'Music Hall',
'Theater',
'Wardroom',
'Closet',
'War Room',
'Bedchamber',
'Cloakroom',
'Dressing Room',
'Studio',
'Linen Room',
'Boudoir',
'Refectory',
'Sewing Room',
'Buttery',
'Lavatory',
'Bakery',
]

MAX_X = 20
MAX_Y = 20
CREATE_RATE = 0.75
CONNECTION_RATE = 0.9


class Command(BaseCommand):
    def handle(self, *args, **options):

        floor = Floor(name=f'1st Floor', level=0, num_rooms=0)
        floor.save()
        total_rooms = 0
        
        # Create the rooms
        for x in range(MAX_X):
            for y in range(MAX_Y):
                if random.random() <= CREATE_RATE:
                    room = Room(name = f'{random.choice(room_names)}', description=room_descriptions.pop(), floor=floor, pos_x=x, pos_y=y, connections=0)
                    room.save()
                    total_rooms += 1
        floor.num_rooms = total_rooms
        floor.save()

        # Connect the rooms
        for x in range(MAX_X):
            for y in range(MAX_Y):
                # Is there a room?
                room = Room.objects.filter(pos_x=x, pos_y=y).first()
                if room is not None:
                    # Try to connect north, if you are not at the top of the map and there is a room above
                    if y + 1 < MAX_Y and Room.objects.filter(pos_x=x, pos_y=y+1).first() and random.random() <= CONNECTION_RATE:
                        room.connection_north = Room.objects.get(pos_x=x, pos_y=y+1)
                        room.connections += 1
                        room.save()
                    # Try to connect south, if you are not at the bottom of the map and there is a room below
                    if y - 1 >= 0 and Room.objects.filter(pos_x=x, pos_y=y-1).first() and random.random() <= CONNECTION_RATE:
                        room.connection_south = Room.objects.get(pos_x=x, pos_y=y-1)
                        room.connections += 1
                        room.save()

                    # Try to connect east, if you are not at the east most position (max) and there is a room to the east
                    if x + 1 < MAX_X and Room.objects.filter(pos_x=x+1, pos_y=y).first() and random.random() <= CONNECTION_RATE:
                        room.connection_east = Room.objects.get(pos_x=x+1, pos_y=y)
                        room.connections += 1
                        room.save()

                    # Try to connect west, if you are not at the west most position (0) and there is room to the west
                    if x - 1 >= 0 and Room.objects.filter(pos_x=x-1, pos_y=y).first() and random.random() <= CONNECTION_RATE:
                        room.connection_west = Room.objects.get(pos_x=x-1, pos_y=y)
                        room.connections += 1
                        room.save()
        