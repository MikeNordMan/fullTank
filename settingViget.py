import tkinter
from tkinter import *
import json


class SettingsPump(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.timeMax = 100  # Время работы скважены max(мин)
        self.timeRecicle = 54  # Время работы восстановления скважены (мин)
        self.powerPump = 6  # Мощность насоса
        self.rainSensor = IntVar()  # состояние чекбокса Датчик дождя
        self.vTank = 2500 # объем емкости
        self.list_data = [] # список данных для передачи в файл
        self.file_data = 'test.json' # файл для записи и чтения данных
        #self.read_data()
        self.bild_data(self.read_data())
        self.bildFrame()


    def bildFrame(self):
        self.main_frame = Frame(borderwidth=1, relief=SOLID, pady=5, padx=1)
        self.heading_frame = Frame(self.main_frame, pady=5, padx=5)
        self.tm_frame = Frame(self.main_frame, pady=5, padx=1)
        self.tr_frame = Frame(self.main_frame, pady=5, padx=1)
        self.pp_frame = Frame(self.main_frame, pady=5, padx=1)
        self.rs_frame = Frame(self.main_frame, pady=5, padx=1)
        self.vt_frame = Frame(self.main_frame, pady=5, padx=1)
        self.btn_frame = Frame(self.main_frame, pady=5, padx=1)

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

        self.vt_label = Label(self.vt_frame, text='Объем емкости (л)')
        self.vt_entry = Entry(self.vt_frame, width=4, textvariable=self.vTank)
        self.vt_entry.insert(4, str(self.vTank))

        self.btn = Button(self.btn_frame, text='Применить', command=self.save_change)

        self.main_frame.pack()
        self.heading_frame.pack()

        self.tm_frame.pack(fill=BOTH, expand=True)
        self.tm_frame['width'] = 259

        self.tr_frame.pack(fill=BOTH, expand=True)
        self.tr_frame['width'] = 259

        self.pp_frame.pack(fill=BOTH, expand=True)
        self.pp_frame['width'] = 259

        self.vt_frame.pack(fill=BOTH, expand=True)
        self.vt_frame['width'] = 259

        self.rs_frame.pack(fill=BOTH, expand=True)
        self.rs_frame['width'] = 259

        self.btn_frame.pack(fill=BOTH, expand=True)
        self.btn_frame['width'] = 259

        self.heading_label.pack(fill=X)
        self.tm_label.pack(side=LEFT, anchor=W)
        self.tm_entry.pack(anchor=E)
        self.tr_label.pack(side=LEFT)
        self.tr_entry.pack()
        self.pp_label.pack(side=LEFT)
        self.pp_entry.pack(anchor=E)
        self.vt_label.pack(side=LEFT)
        self.vt_entry.pack(anchor=E)
        self.rs_label.pack(side=LEFT)
        self.rs_checkBtn.pack(anchor=E)
        self.btn.pack()

        '''-------Колибровка------------'''
        #self.tm_frame.update()
        #print(self.tm_frame.winfo_width())
        #self.tr_frame.update()
        #print(self.tr_frame.winfo_width())
        #self.pp_frame.update()
        #print(self.pp_frame.winfo_width())
        #self.rs_frame.update()
        #print(self.rs_frame.winfo_width())
        '''------------------------------'''
    def show_check(self): #Пока для визуализации
              print('On' if self.rainSensor.get() == 1 else 'Off')

    def save_change(self):# Метод сохранения данных
        self.list_data = [int(self.getTimeMax()),
                          int(self.getTimeRecicle()),
                          int(self.getPowerPump()),
                          int(self.getVTank()),
                          self.getRainSensor()]
        print('Сохранено')
        print('Данные для записи:')
        print(self.list_data)
        self.write_data(self.list_data)

    def write_data(self, list_date):
        with open(self.file_data, "w") as f:
            json.dump(list_date, f)

    def read_data(self):
        try:
            with open(self.file_data, "r") as f:
                data_loaded = json.load(f)
            print(data_loaded)
            return data_loaded
        except: print("Нет данных пока! Пропускаем")

    def bild_data(self, data_loaded):
        self.timeMax = data_loaded[0]
        self.timeRecicle = data_loaded[1]
        self.powerPump = data_loaded[2]
        self.vTank = data_loaded[3]
        self.rainSensor.set(data_loaded[4])


    def setTimeMax(self, timeMax):
        self.timeMax = timeMax

    def setTimeRecicle(self, timeRecicle):
        self.timeRecicle = timeRecicle

    def setPowerPump(self, powerPump):
        self.powerPump = powerPump

    def setRainSensor(self, rainSensor):
        self.rainSensor.set(rainSensor)

    def getTimeMax(self):
        timeMax = self.tm_entry.get()
        return timeMax

    def getTimeRecicle(self):
        timeRecicle = self.tr_entry.get()
        return timeRecicle

    def getPowerPump(self):
        powerPump = self.pp_entry.get()
        return powerPump

    def getVTank(self):
        vTank = self.vt_entry.get()
        return vTank

    def getRainSensor(self):
        return self.rainSensor.get()
