# hotel model
from room import Room


class Hotel:
    def __init__(self, name='x', location='x'):
        self.name = name
        self.location = location
        self.rooms = []

    def __str__(self):
        r = 'Hotel Name : {}\n' \
            'Number of Rooms : {}\n' \
            'Number of Occupied Rooms : {}\n\n' \
            'Room Details are:\n\n'.format(self.name,
                                           len(self.rooms),
                                           len(self.reservation))
        for val in self.rooms:
            r += '{}\n'.format(str(val))

        return r

    # bool - all full
    @property
    def is_full(self):
        b = True
        for r in self.rooms:
            if r.occupied is False:
                b = False
                break
        return b

    # bool - all empty
    @property
    def is_empty(self):
        b = True
        for r in self.rooms:
            if r.occupied is True:
                b = False
                break
        return b

    # add a room to the hotel
    def add_room(self, number=0, occupant='Not Occupied', smoking='n', bed_type='twin', rate=0.0):
        self.rooms.append(Room(number, occupant, smoking, bed_type, rate))

    # list - get all reserved rooms
    @property
    def reservation(self):
        rooms = []
        for r in self.rooms:
            if r.occupied is True:
                rooms.append(r)
        return rooms

    # tuple -  add reservation
    @reservation.setter
    def reservation(self, tup=('name', 'n', 'twin')):
        found = 'NO EMPTY ROOMS\n'
        for r in self.rooms:
            if r.occupied is False and r.smoking == tup[1] and r.bed_type == tup[2]:
                r.occupant = tup[0]
                r.occupied = True
                found = 'room {} reserved for {}\n'.format(r.room_number, r.occupant)
                break
        print(found)

    # list -  get all empty rooms
    @property
    def unoccupied(self):
        rooms = []
        for r in self.rooms:
            if r.occupied is False:
                rooms.append(r)
        return rooms

    # str - cancel reservation
    @unoccupied.setter
    def unoccupied(self, occupant):
        found = 'NOT FOUND\n'
        for r in self.rooms:
            if r.occupant.lower() == occupant.lower():
                r.occupant = 'Not Occupied'
                r.occupied = False
                found = 'reservation cancelled\n'
                break
        print(found)

    # list[room->object]- get reservation
    def find_reservation(self, name):
        found = 'NOT FOUND\n'
        for r in self.rooms:
            if r.occupant == name:
                found = r
        return found

    # int - occupied count getter
    @property
    def occupied_count(self):
        oc = 0
        for r in self.rooms:
            if r.occupied is True:
                oc += 1
        return oc

    @property
    def get_daily_sales(self):
        total = 0.0
        for r in self.reservation:
            if r.occupied is True:
                total+=r.rate
        return total

    @property
    def get_occupancy_percent(self):
        return (self.occupied_count / len(self.rooms))*100