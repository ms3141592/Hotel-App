# hotel model
from db_controller import MySQL_CRUD
from room import Room


class Hotel:
    def __init__(self, name='x', location='x'):
        self.name = name
        self.location = location
        self.rooms = []

        self.initialize_db(name)

    def __str__(self):
        r = 'Hotel Name : {}\n' \
            'Number of Rooms : {}\n' \
            'Number of Occupied Rooms : {}\n\n' \
            'Room Details are:\n\n' \
            'room\tname\tsmoking\tbed\trate\n' \
            '----\t----\t-------\t---\t----\n' \
            '{}'.format(self.name, len(self.rooms),'0', self.db.show_db_table('rooms','number'))
        return r

    def daily_sales(self):
        return '$ {}'.format(self.db.get_daily_sales('rooms', 'occupied'))

    def room_status(self):
        return self.db.show_db_table_stat('rooms', 'occupied')


    def daily_percentage(self):
        return '% {:.2f}'.format(self.db.percentage('rooms', 'occupied'))


    def initialize_db(self, name):
        self.db = MySQL_CRUD('localhost', 'root', 'root')
        n = name.replace(' ', '_')
        self.db.create_db(n)
        self.db.create_db_table('accounts',
                                'user_name VARCHAR(16) NOT NULL,'
                                'password VARCHAR(16) NOT NULL,'
                                'admin VARCHAR(1) NOT NULL')
        self.db.create_db_table('rooms',
                                'number INT NOT NULL,'
                                'occupant VARCHAR(16) NOT NULL,'
                                'smoking VARCHAR(1) NOT NULL,'
                                'bed VARCHAR(5) NOT NULL,'
                                'rate FLOAT NOT NULL,'
                                'occupied VARCHAR(1) NOT NULL')


    def hotel_info(self):
        return
    # add a room to the hotel
    def add_room(self, number=0, occupant='None', smoking='n', bed_type='twin', rate=0.0, occupied=0):
        #self.rooms.append(Room(number, occupant, smoking, bed_type, rate))

        self.db.insert_into_db((number,occupant,smoking,bed_type,rate,occupied), 'rooms')

    def add_reservation(self, name, smoking, bed, res):
        if res is 2:
            self.db.edit_table_row('rooms', 'occupant', name, 'None','bed', bed, 'smoking',smoking)
            print(name, bed, smoking)
        if res is 1:
            self.db.edit_row('rooms', 'occupant', name, 'None')
            print('cancel')

    def cancel_reservation(self, name):
        self.db.edit_row('rooms', 'occupant', name, 'None')


    # list[room->object]- get reservation
    def find_reservation(self, var):
        #found = 'NOT FOUND\n'
        #for r in self.rooms:
        #    if r.occupant == var:
        #        found = r
        #return found
        return self.db.show_db_table('rooms', var)


    """
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
    """
