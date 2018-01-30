"""
hotel managment gui - not functional or connected to db
"""
# TODO:: need comments explaining what everything does
# TODO:: connect to Hotel class
# TODO:: connect to db


import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image

from hotel import Hotel


class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


class HotelController(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.resizable(width=False, height=False)
        tk.Tk.iconbitmap(self, default='images/logo.ico')
        tk.Tk.wm_title(self, 'Hotel Management App')

        container = tk.Frame(self)
        container.grid(columnspan=10, padx=10, pady=10)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for fr in (FrameDisplay, Page2):
            frame = fr(container, self)
            self.frames[fr] = frame

            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(FrameDisplay)

    def show_frame(self, cntlr):
        frame = self.frames[cntlr]
        frame.tkraise()


class FrameDisplay(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.int = None
        self.reserved = None
        self.hotel = Hotel('Beach Marriot Pensacola',
                           '123 Main Street, City, ST 10000')
        # self.define_room(number=1, occupant='empty', smoking='s', bed='twin', rate=1.1, occupied=1, reservation=1)
        self.run()

    def menu_bar(self):
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="home", command=lambda: self.login_page())
        filemenu.add_command(label="print", command=lambda: self.print_page())
        filemenu.add_separator()
        filemenu.add_command(label="exit", command=lambda: exit())
        menubar.add_cascade(label="menu", menu=filemenu)

        admin_menu = tk.Menu(menubar, tearoff=0)
        admin_menu.add_command(label="add user", command=lambda: self.add_user())
        admin_menu.add_command(label="modify hotel", command=lambda: self.modify_hotel())
        menubar.add_cascade(label="admin", menu=admin_menu)

        hotel_menu = tk.Menu(menubar, tearoff=0)
        hotel_menu.add_command(label="info", command=lambda: self.hotel_info())
        hotel_menu.add_command(label="current rooms", command=lambda: self.current_rooms())
        hotel_menu.add_command(label="check reservation", command=lambda: self.reservation_status())
        hotel_menu.add_command(label="room reservation", command=lambda: self.room_reservation())
        menubar.add_cascade(label="hotel", menu=hotel_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="help", command=lambda: self.add_user())
        menubar.add_cascade(label="help", menu=help_menu)

        self.controller.config(menu=menubar)

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    def run(self):
        self.define_room(number=1, occupant='empty', smoking='s', bed='twin', rate=1.1, occupied=1, reservation=1)
        self.login_page()
        self.menu_bar()

    def print_page(self):
        pass

    def define_room(self, number=None, occupant=None, smoking=None, bed=None, rate=None, occupied=None,
                    reservation=None):
        if reservation:
            self.reservation = reservation
        if number:
            self.number = number
        if occupant:
            self.occupant = occupant
        if smoking:
            self.smoking = smoking
        if bed:
            self.bed = bed
        if rate:
            self.rate = rate
        if occupied:
            self.occupied = occupied

    #########################
    # main page on start    #
    #########################
    def login_page(self):
        self.clear_frame()
        label = ttk.Label(self, text='login page')
        label.grid(row=0, column=0, columnspan=10, pady=10, padx=10)

        login_btn = ttk.Button(self, text='login',
                               command=lambda: print('p'))
        login_btn.grid(row=2, column=5, pady=2, padx=2)

        un_label = ttk.Label(self, text='username')
        un_label.grid(row=2, column=0, padx=1, pady=1)
        un_entry = ttk.Entry(self, textvariable='user_log', width=25)
        un_entry.grid(row=2, column=2, pady=1)

        pw_label = ttk.Label(self, text='password')
        pw_label.grid(row=2, column=3, padx=1, pady=1)
        pw_entry = ttk.Entry(self, textvariable='user_pw', width=25, show='*')
        pw_entry.grid(row=2, column=4, pady=1)

        img = ImageTk.PhotoImage(Image.open('images\hotel_clipart.png'))
        img_label = ttk.Label(self, image=img)
        img_label.image = img
        img_label.grid(row=3, column=0, columnspan=6, padx=20, pady=20)
        self.menu_bar()

    #########################
    # admin page            #
    #########################
    def add_user(self):
        self.clear_frame()
        label = ttk.Label(self, text='')
        label.grid(row=2, column=0, columnspan=10, pady=10, padx=10)
        label = ttk.Label(self, text='add user')
        label.grid(row=3, column=0, columnspan=10, pady=10, padx=10)

        un_label = ttk.Label(self, text='username')
        un_label.grid(row=4, column=0, padx=1, pady=1)
        un_entry = ttk.Entry(self, textvariable='new_user', width=25)
        un_entry.grid(row=4, column=1, pady=1)
        pw_label = ttk.Label(self, text='password')
        pw_label.grid(row=4, column=2, padx=1, pady=1)
        pw_entry = ttk.Entry(self, textvariable='new_pw', width=25)
        pw_entry.grid(row=4, column=3, pady=1)

        var = tk.IntVar()
        admin_radio = ttk.Radiobutton(self, text='admin',
                                      variable=var,
                                      value=1,
                                      command=lambda: print('admin'))
        admin_radio.grid(row=5, column=0, padx=1, pady=3)
        employee_radio = ttk.Radiobutton(self, text='employee',
                                         variable=var,
                                         value=2,
                                         command=lambda: print('employee'))
        employee_radio.grid(row=5, column=1, padx=1, pady=3)

        create = ttk.Button(self, text='add',
                            command=lambda: print('added'))
        create.grid(row=5, column=2, columnspan=3, padx=1, pady=3)
        self.menu_bar()

    def eddit_room(self, num=0, rate=0):
        self.hotel.add_room(number=num, occupant=self.occupant, smoking=self.smoking, bed_type=self.bed, rate=rate,
                            occupied=1)

    def modify_hotel(self):
        self.clear_frame()
        label = ttk.Label(self, text='')
        label.grid(row=2, column=0, columnspan=10, pady=10, padx=10, sticky='w')
        label = ttk.Label(self, text='room modification')
        label.grid(row=2, column=0, columnspan=10, pady=10, padx=10, sticky='W')

        var = tk.IntVar()
        edit_radio = ttk.Radiobutton(self, text='edit room',
                                     variable=var,
                                     value=1,
                                     command=lambda: print('edit room'))
        edit_radio.grid(row=4, column=0, columnspan=3, padx=1, pady=5, sticky='w')
        add_radio = ttk.Radiobutton(self, text='add room',
                                    variable=var,
                                    value=1,
                                    command=lambda: print('add room'))
        add_radio.grid(row=4, column=1, columnspan=3, padx=1, pady=5, sticky='w')

        label = ttk.Label(self, text='')
        label.grid(row=5, column=0, columnspan=10, pady=10, padx=10)

        rn_label = ttk.Label(self, text='room number')
        rn_label.grid(row=7, column=0, padx=1, pady=1)
        rn_entry = ttk.Entry(self, textvariable='rn', width=25)
        rn_entry.grid(row=7, column=1, pady=5)

        smk = tk.IntVar()
        s_radio = ttk.Radiobutton(self, text='smoking',
                                  variable=smk,
                                  value=1,
                                  command=lambda: self.define_room(smoking='s'))
        s_radio.grid(row=8, column=0, padx=1, pady=5, sticky='w')
        non_s_radio = ttk.Radiobutton(self, text='non-smiking',
                                      variable=smk,
                                      value=2,
                                      command=lambda: self.define_room(smoking='n'))
        non_s_radio.grid(row=8, column=1, padx=1, pady=5, sticky='w')

        bed = tk.IntVar()
        admin_radio = ttk.Radiobutton(self, text='twin',
                                      variable=bed,
                                      value=1,
                                      command=lambda: self.define_room(bed='twin'))
        admin_radio.grid(row=9, column=0, padx=1, pady=5, sticky='w')
        employee_radio = ttk.Radiobutton(self, text='queen',
                                         variable=bed,
                                         value=2,
                                         command=lambda: self.define_room(bed='queen'))
        employee_radio.grid(row=9, column=1, padx=1, pady=5, sticky='w')
        employee_radio = ttk.Radiobutton(self, text='king',
                                         variable=bed,
                                         value=3,
                                         command=lambda: self.define_room(bed='king'))
        employee_radio.grid(row=9, column=1, padx=1, pady=5, sticky='e')

        rate_label = ttk.Label(self, text='rate')
        rate_label.grid(row=10, column=0, padx=1, pady=5, sticky='w')
        rate_entry = ttk.Entry(self, textvariable='rate', width=25)
        rate_entry.grid(row=10, column=1, pady=5, sticky='w')

        create = ttk.Button(self, text='confirm',
                            command=lambda: self.eddit_room(num=rn_entry.get(), rate=rate_entry.get()))
        create.grid(row=11, column=0, padx=1, pady=5, sticky='w')
        self.menu_bar()

    #########################
    # hotel page            #
    #########################
    def hotel_info_type(self, int=None):
        if int:
            self.int = int

        hotel_info = ttk.Button(self, text='hotel info', command=lambda: self.hotel_info_type(1))
        hotel_info.grid(row=0, column=0, columnspan=3, padx=1, pady=5, sticky='w')
        daily_sales = ttk.Button(self, text='daily sales', command=lambda: self.hotel_info_type(2))
        daily_sales.grid(row=0, column=0, columnspan=3, padx=1, pady=5, sticky='ns')
        occupancy = ttk.Button(self, text='occupancy percentage', command=lambda: self.hotel_info_type(3))
        occupancy.grid(row=0, column=0, columnspan=3, padx=1, pady=5, sticky='e')
        empty_info = tk.Text(self, height=32, width=70)
        empty_scroll = ttk.Scrollbar(self, command=empty_info.yview)
        empty_info.configure(yscrollcommand=empty_scroll.set)

        empty_info.insert(tk.END, self.display_info())
        empty_info.config(state=tk.DISABLED)

        empty_info.grid(row=2, column=0)
        empty_scroll.grid(row=2, column=1, rowspan=10, sticky='nswe')

    def display_info(self):
        if self.int is 1:
            return str(self.hotel)
        elif self.int is 2:
            return self.hotel.daily_sales()
        elif self.int is 3:
            return self.hotel.daily_percentage()
        else:
            return 'info'

    def hotel_info(self):
        self.clear_frame()

        self.hotel_info_type()

        self.menu_bar()

    def current_rooms(self):
        self.clear_frame()
        e, f = self.hotel.room_status()
        label = ttk.Label(self, text='empty rooms')
        label.grid(row=0, column=0, columnspan=10, pady=10, padx=10, sticky='w')
        label = ttk.Label(self, text='reserved rooms')
        label.grid(row=0, column=2, columnspan=10, pady=10, padx=10, sticky='w')

        empty_info = tk.Text(self, height=32, width=34)
        empty_scroll = ttk.Scrollbar(self, command=empty_info.yview)
        empty_info.configure(yscrollcommand=empty_scroll.set)

        empty_info.insert(tk.END, e)
        empty_info.config(state=tk.DISABLED)

        empty_info.grid(row=2, column=0)
        empty_scroll.grid(row=2, column=1, rowspan=10, sticky='nswe')
        self.menu_bar()

        full_info = tk.Text(self, height=32, width=34)
        full_scroll = ttk.Scrollbar(self, command=full_info.yview)
        full_info.configure(yscrollcommand=full_scroll.set)

        full_info.insert(tk.END, f)
        full_info.config(state=tk.DISABLED)

        full_info.grid(row=2, column=2)
        full_scroll.grid(row=2, column=3, rowspan=10, sticky='nswe')

    def reservation_status(self):
        self.clear_frame()

        self.find_reservation()

        self.menu_bar()

    def room_reservation(self):
        self.clear_frame()

        label = ttk.Label(self, text='')
        label.grid(row=2, column=0, columnspan=10, pady=10, padx=10, sticky='w')
        label = ttk.Label(self, text='room reservation')
        label.grid(row=2, column=0, columnspan=10, pady=10, padx=10, sticky='w')

        var = tk.IntVar()
        create_radio = ttk.Radiobutton(self, text='create reservation',
                                       variable=var,
                                       value=1,
                                       command=lambda: self.define_room(reservation=2))
        create_radio.grid(row=4, column=0, columnspan=3, padx=1, pady=5, sticky='w')
        cancel_radio = ttk.Radiobutton(self, text='cancel reservation',
                                       variable=var,
                                       value=2,
                                       command=lambda: self.define_room(reservation=1))
        cancel_radio.grid(row=4, column=1, columnspan=3, padx=1, pady=5, sticky='e')

        label = ttk.Label(self, text='')
        label.grid(row=5, column=0, columnspan=10, pady=10, padx=10)

        n_label = ttk.Label(self, text='guest name')
        n_label.grid(row=7, column=0, padx=1, pady=1)
        n_entry = ttk.Entry(self, textvariable='entry', width=25)
        n_entry.grid(row=7, column=1, pady=5)

        smk = tk.IntVar()
        s_radio = ttk.Radiobutton(self, text='smoking',
                                  variable=smk,
                                  value=1,
                                  command=lambda: self.define_room(smoking='s'))
        s_radio.grid(row=8, column=0, padx=1, pady=5, sticky='w')
        n_radio = ttk.Radiobutton(self, text='non-smiking',
                                  variable=smk,
                                  value=2,
                                  command=lambda: self.define_room(smoking='n'))
        n_radio.grid(row=8, column=1, padx=1, pady=5, sticky='w')

        bed = tk.IntVar()
        admin_radio = ttk.Radiobutton(self, text='twin',
                                      variable=bed,
                                      value=1,
                                      command=lambda: self.define_room(bed='twin'))
        admin_radio.grid(row=9, column=0, padx=1, pady=5, sticky='w')
        employee_radio = ttk.Radiobutton(self, text='queen',
                                         variable=bed,
                                         value=2,
                                         command=lambda: self.define_room(bed='queen'))
        employee_radio.grid(row=9, column=1, padx=1, pady=5, sticky='w')
        employee_radio = ttk.Radiobutton(self, text='king',
                                         variable=bed,
                                         value=3,
                                         command=lambda: self.define_room(bed='king'))
        employee_radio.grid(row=9, column=1, padx=1, pady=5, sticky='e')

        create = ttk.Button(self, text='confirm',
                            command=lambda: self.hotel.add_reservation(name=n_entry.get(), smoking=self.smoking,
                                                                       bed=self.bed, res=self.reservation))
        create.grid(row=10, column=0, padx=1, pady=5, sticky='w')
        self.menu_bar()

    def find_reservation(self, val='null', key='null'):

        self.reserved = self.hotel.check_reservation('rooms', val, key)

        label = ttk.Label(self, text='')
        label.grid(row=2, column=0, columnspan=10, pady=10, padx=10, sticky='w')
        label = ttk.Label(self, text='room reservation')
        label.grid(row=2, column=0, columnspan=10, pady=10, padx=10, sticky='w')

        res_entry = ttk.Entry(self, textvariable='res entry', width=25)
        res_entry.grid(row=5, column=0, padx=1, pady=5, sticky='w')
        check_nm = ttk.Button(self, text='name',
                              command=lambda: self.find_reservation(res_entry.get(), 'occupant'))
        check_nm.grid(row=5, column=0, padx=1, pady=5, sticky='n')
        check_rm = ttk.Button(self, text='room',
                              command=lambda: self.find_reservation(res_entry.get(), 'number'))
        check_rm.grid(row=5, column=0, padx=1, pady=5, sticky='e')

        empty_info = tk.Text(self, height=28, width=70)
        empty_scroll = ttk.Scrollbar(self, command=empty_info.yview)
        empty_info.configure(yscrollcommand=empty_scroll.set)

        empty_info.insert(tk.END, self.display_reservation())
        empty_info.config(state=tk.DISABLED)

        empty_info.grid(row=10, column=0)
        empty_scroll.grid(row=10, column=1, rowspan=10, sticky='nswe')

    def display_reservation(self):
        r = 'no reservation'
        if self.reserved:
            r=''
            for res in self.reserved:
                r += '{} '.format(res)

            r = r[0:-2]
            return r
        else:
            return r