import tkinter
from tkinter import *


class SettingsPump(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.timeMax = 100  # Время работы скважены max(мин)
        self.timeRecicle = 54  # Время работы восстановления скважены (мин)
        self.powerPump = 6  # Мощность насоса
        self.rainSensor = IntVar()  # состояние чекбокса Датчик дождя
        self.bildFrame()

    def bildFrame(self):
        self.main_frame = Frame(borderwidth=1, relief=SOLID, pady=5, padx=1)
        self.heading_frame = Frame(self.main_frame, pady=5, padx=5)
        self.tm_frame = Frame(self.main_frame, pady=5, padx=1)
        self.tr_frame = Frame(self.main_frame, pady=5, padx=1)
        self.pp_frame = Frame(self.main_frame, pady=5, padx=1)
        self.rs_frame = Frame(self.main_frame, pady=5, padx=1)

        self.heading_label = Label(self.heading_frame, text='Настройки Системы')
        self.tm_label = Label(self.tm_frame, text='Дебет скважены (л) ')
        self.tm_entry = Entry(self.tm_frame, width=4, textvariable=self.timeMax)
        self.tm_entry.insert(1, str(self.timeMax))

        self.tr_label = Label(self.tr_frame, text='Время восстановления скважены (мин)')
        self.tr_entry = Entry(self.tr_frame, width=4, textvariable=self.timeRecicle)
        self.tr_entry.insert(2, str(self.timeRecicle))

        self.pp_label = Label(self.pp_frame, text='Мощность насоса л/мин')
        self.pp_entry = Entry(self.pp_frame, width=4, textvariable=self.powerPump)
        self.pp_entry.insert(3, str(self.powerPump))

        self.rs_label = Label(self.rs_frame, text='Датчик дождя ')
        self.rs_checkBtn = Checkbutton(self.rs_frame,  variable=self.rainSensor, command=self.show_check)


        self.main_frame.pack()
        self.heading_frame.pack()
        self.tm_frame.pack(fill=BOTH, expand=True)
        self.tm_frame['width'] = 259
        self.tr_frame.pack(fill=BOTH, expand=True)
        self.tr_frame['width'] = 259
        self.pp_frame.pack(fill=BOTH, expand=True)
        self.pp_frame['width'] = 259
        self.rs_frame.pack(fill=BOTH, expand=True)
        self.rs_frame['width'] = 259

        self.heading_label.pack(fill=X)
        self.tm_label.pack(side=LEFT, anchor=W)
        self.tm_entry.pack(anchor=E)
        self.tr_label.pack(side=LEFT)
        self.tr_entry.pack()
        self.pp_label.pack(side=LEFT)
        self.pp_entry.pack(anchor=E)
        self.rs_label.pack(side=LEFT)
        self.rs_checkBtn.pack(anchor=E)

        '''-------Колибровка------------'''
        self.tm_frame.update()
        print(self.tm_frame.winfo_width())
        self.tr_frame.update()
        print(self.tr_frame.winfo_width())
        self.pp_frame.update()
        print(self.pp_frame.winfo_width())
        self.rs_frame.update()
        print(self.rs_frame.winfo_width())
        '''------------------------------'''
    def show_check(self):
              print('On' if self.rainSensor.get() == 1 else 'Off')

    def setTimeMax(self, timeMax):
        self.timeMax = timeMax

    def setTimeRecicle(self, timeRecicle):
        self.timeRecicle = timeRecicle

    def setPowerPump(self, powerPump):
        self.powerPump = powerPump

    def setRainSensor(self, rainSensor):
        self.rainSensor = rainSensor

    def getTimeMax(self):
        return self.timeMax

    def getTimeRecicle(self):
        return self.timeRecicle

    def getPowerPump(self):
        return self.powerPump

    def getRainSensor(self):
        return self.rainSensor.get()