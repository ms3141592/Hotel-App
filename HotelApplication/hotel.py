# hotel model
from db_controller import MySQL_CRUD



class Hotel:
    def __init__(self, name='x', location='x'):
        self.name = name
        self.location = location
        self.rooms = []

        self.initialize_db(name)

    def __str__(self):
        i,j = self.db.show_db_table('rooms','number')
        a,b=0,0
        for k in j:
            if k == '2':
                a += 1
                b += 1
            if k == '1':
                a+=1

        r = 'hotel name : {}\n' \
            'number of rooms : {}\n' \
            'number of occupied rooms : {}\n\n' \
            'room details are:\n\n' \
            'room\toccupant name\t\t\tsmoking\tbed\trate\n' \
            '----\t-------------\t\t\t-------\t---\t----\n' \
            '{}'.format(self.name, a,b, i)
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
                                'user_name VARCHAR(16) NOT NULL UNIQUE,'
                                'password VARCHAR(20) NOT NULL,'
                                'admin VARCHAR(1) NOT NULL')
        self.db.create_db_table('rooms',
                                'number INT NOT NULL UNIQUE,'
                                'occupant VARCHAR(20) NOT NULL,'
                                'smoking VARCHAR(1) NOT NULL,'
                                'bed VARCHAR(5) NOT NULL,'
                                'rate FLOAT NOT NULL,'
                                'occupied VARCHAR(1) NOT NULL')


    # add a room to the hotel
    def add_room(self, number=0, occupant='empty', smoking='n', bed_type='twin', rate=0.0, occupied=0):
        self.db.insert_into_db((number,occupant,smoking,bed_type,rate,occupied), 'rooms')

    def add_reservation(self, name, smoking, bed, res):
        if res is 2:
            self.db.edit_table_row('rooms', 'occupant', name, 'empty','bed', bed, 'smoking',smoking)

        if res is 1:
            self.db.edit_row('rooms', 'occupant', name, 'empty')


    def cancel_reservation(self, name):
        self.db.edit_row('rooms', 'occupant', name, 'empty')


    def find_reservation(self, var):
        return self.db.show_db_table('rooms', var)

    def check_reservation(self, rooms, val, key):
        return self.db.tb_row(rooms, val, key)