from django.core.management.base import BaseCommand, CommandError
from dungeonroom.models import Floor, Room
import random
import pickle


random.seed(5)

# room_descriptions = pickle.load(open('../../../../room_descriptions.p', 'rb'))
room_descriptions = pickle.load(open('../room_descriptions.p', 'rb'))



class Command(BaseCommand):
    def handle(self, *args, **options):
        floor_names = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st', '32nd', '33rd', '34th', '35th', '36th', '37th', '38th', '39th', '40th', '41st', '42nd', '43rd', '44th', '45th', '46th', '47th', '48th', '49th', '50th', '51st', '52nd', '53rd', '54th', '55th', '56th', '57th', '58th', '59th', '60th', '61st', '62nd', '63rd', '64th', '65th', '66th', '67th', '68th', '69th', '70th', '71st', '72nd', '73rd', '74th', '75th', '76th', '77th', '78th', '79th', '80th', '81st', '82nd', '83rd', '84th', '85th', '86th', '87th', '88th', '89th', '90th', '91st', '92nd', '93rd', '94th', '95th', '96th', '97th', '98th', '99th', '100th']

        directions = ['North', 'North East', 'East', 'South East', 'South', 'South West', 'West', 'North West']

        
        for i in range(1,101):
            floor = Floor(name=f'{floor_names[i-1]} Floor', level=i, num_rooms=0)
            floor.save()
            
            total_rooms = 0
            for direction in directions:
                if random.random() < 0.65:
                    room = Room(name = f'{direction} Room', description=room_descriptions.pop(), floor=floor)
                    room.save()
                    total_rooms += 1
            floor.num_rooms = total_rooms
            floor.save()
            # TODO Go back and add logic that guarantees a room for each floor
        