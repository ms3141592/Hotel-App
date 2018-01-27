# hotel view/controller - tester - no exceptions for tester
# TODO:: needs exceptions for user input
from hotel import Hotel


class HotelTestApp:
    def __init__(self):
        self.h = Hotel('Beach Marriot Pensacola', '123 Main Street, City, ST 10000')

        # if a DB was set up the rooms would be added here
        # self.h.add_room(number=101, smoking='s', bed_type='queen', rate=100.00)
        # self.h.add_room(number=102, smoking='n', bed_type='king', rate=110.00)
        # self.h.add_room(number=103, smoking='s', bed_type='king', rate=88.00)
        # self.h.add_room(number=104, smoking='s', bed_type='twin', rate=100)
        # self.h.add_room(number=105, smoking='n', bed_type='queen', rate=99)

        self.menu = {'0': 'self.add_a_room()',
                     '1': 'self.view_hotel_info()',
                     '2': 'self.view_empty_rooms()',
                     '3': 'self.view_full_rooms()',
                     '4': 'self.check_reservation()',
                     '5': 'self.add_reservation()',
                     '6': 'self.remove_reservation()',
                     '7': 'self.view_daily_sales()',
                     '8': 'self.view_occ_percent()'
                     }

    def add_a_room(self):
        num = int(input('add room number:\n'))
        smoking = input('s for smoking, n for non-smoking:\n')
        bed_type = input('bed type (twin, queen, king)\n')
        rate = float(input('room rate:\n'))
        self.h.add_room(number=num, smoking=smoking, bed_type=bed_type, rate=rate)

    def view_hotel_info(self):
        print(str(self.h))

    def view_empty_rooms(self):
        print('unoccupied:\n', *self.h.unoccupied)

    def view_full_rooms(self):
        print('occupied:\n', *self.h.reservation)

    def check_reservation(self):
        r = input('check reservation for:\n')
        print('reservation:\n{}'.format(self.h.find_reservation(r)))

    def add_reservation(self):
        name = input('enter name:\n')
        smoking = input('(s)moking or (n)on-smoking:\n')
        bed_type = input('bed: twin, queen, king:\n')
        self.h.reservation = name, smoking, bed_type

    def remove_reservation(self):
        name = input('enter name to cancel reservation:\n')
        self.h.unoccupied = name

    def view_daily_sales(self):
        print('daily sales: {:.2f}\n'.format(self.h.get_daily_sales))

    def view_occ_percent(self):
        print('occupancy percentage: %{:.3f}\n'.format(int(self.h.get_occupancy_percent)))

    def run_test(self):
        while True:
            print('Hotel reservation test\n'
                  '0. add a room\n'
                  '1. view current info\n'
                  '2. view empty rooms\n'
                  '3. view full rooms\n'
                  '4. check reservation\n'
                  '5. add reservation\n'
                  '6. remove reservation\n'
                  '7. view daily sales\n'
                  '8. view occupancy percentage\n'
                  '9. close test\n')
            c = input('>')
            if c is '9':
                # this is were the rooms would be saved to a DB
                break
            for k,v in self.menu.items():
                if c is k:
                    eval(v) # get method out of string


if __name__ == '__main__':
    print('...')
    HotelTestApp().run_test()
