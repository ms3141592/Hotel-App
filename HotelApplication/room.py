# room model


class Room:
    def __init__(self, num, occupant, smoking, bed_type, rate):
        self.number = num
        self.occupant = occupant
        self.smoking = smoking
        self.bed_type = bed_type
        self.rate = rate
        self.occupied = False

    def __str__(self):
        return 'Room Number: {}\n' \
               'Occupant Name: {}\n' \
               'Smoking Room: {}\n' \
               'Bed Type: {}\n' \
               'Rate: {:.2f}\n'.format(self.number,
                                       self.occupant,
                                       self.smoking,
                                       self.bed_type,
                                       self.rate)

    # getter and setters
    @property
    def room_bed_type(self):
        return self.bed_type

    @room_bed_type.setter
    def room_bed_type(self, val):
        self.bed_type = val

    @property
    def room_smoking(self):
        return self.smoking

    @room_smoking.setter
    def room_smoking(self, val):
        self.smoking = val

    @property
    def room_number(self):
        return self.number

    @room_number.setter
    def room_number(self, val):
        self.number = val

    @property
    def room_rate(self):
        return self.room_rate

    @room_rate.setter
    def room_rate(self, val):
        self.room_rate = val

    @property
    def room_occupant(self):
        return self.occupant

    @room_occupant.setter
    def room_occupant(self, val):
        self.occupant = val

    @property
    def room_occupied(self):
        return self.occupied

    @room_occupied.setter
    def room_occupied(self, val):
        self.occupied = val
