import tkinter
from tkinter import *
from tkinter import ttk


class Progress_Tank(tkinter.Frame):
    def __init__(self, master, infoMsg, connect):
        super().__init__(master)
        self.infoMsg = infoMsg # Экземпляр Инфокласса
        self.connect = connect # Экземпляр Подключения

        self.vTank = 500 # объем танка л
        self.speedPump = 12  # скорость работы насоса л в минуту
        self.speedTankPump = 20 # скорость расхода Танка л в минуту
        self.reainsTank = 50# остаток в танке
        self.vBoreHole = 20  # дебет скважены

        self.flag_on_off = False  # флаг включения насоса
        self.flag_use_tank =False # флаг включения расхода танка
        self.flag_Recovery = False  # флаг востановления скважены
        self.flag_FullTank = False  # флаг полный танк
        self.speed_Rec_BH = 20  # скорость восстановления скважены л в минуту
        self.timer_1 = None
        self.timer_2 = None
        self.timer_3 = None

        self.hightBar = 450 #Высота Progerss-Bar

        self.bildFrame()
        self.fullTank()
        print(self.infoMsg.infoLabel.cget('text'))



    def bildFrame(self):
        self.main_frame = Frame(self.master, borderwidth=1, relief=SOLID, pady=5, padx=1)
        self.heading_frame = Frame(self.main_frame, borderwidth=1, relief=SOLID, pady=5, padx=5)

        '''Главный внутренний Фрейм для данных'''
        self.data_frame = Frame(self.main_frame, borderwidth=1, relief=SOLID, pady=5, padx=5)

        '''Фрейм для заголовка Прогресс бара Танка'''
        self.head_barTank_frame = Frame(self.data_frame, borderwidth=1, relief=SOLID, pady=0, padx=0)

        self.head_Tank = Frame(self.heading_frame, borderwidth=1, relief=SOLID, pady=0, padx=0)
        self.head_BoreHole = Frame(self.heading_frame, borderwidth=1, relief=SOLID, pady=0, padx=0)

        '''Фрейм для Прогресс-бара Танка'''
        self.barTank_frame = Frame(self.data_frame, borderwidth=1, relief=SOLID, pady=2, padx=15)

        '''Фрейм для Прогресс-бара Скважены'''
        self.barBoreHole_frame = Frame(self.data_frame, borderwidth=1, relief=SOLID, pady=2, padx=25)

        self.main_frame.pack()
        self.heading_frame.pack()
        self.head_Tank.pack(side=LEFT, ipadx=20)
        self.head_BoreHole.pack()


        self.data_frame.pack()

        self.head_barTank_frame.pack(side=LEFT, fill=Y)
        self.barTank_frame.pack(side=LEFT)
        self.barBoreHole_frame.pack(side=LEFT)

        '''Фреймы для Заголовков Прогресс-Бара Танка'''
        self.head_barTank_frame_top = Frame(self.head_barTank_frame, borderwidth=1, relief=SOLID, pady=0, padx=0)
        self.head_barTank_frame_middle = Frame(self.head_barTank_frame, borderwidth=1, relief=SOLID, pady=0, padx=0)
        self.head_barTank_frame_foot = Frame(self.head_barTank_frame, borderwidth=1, relief=SOLID, pady=0, padx=0)

        self.head_barTank_frame_top.pack()
        self.head_barTank_frame_middle.pack()
        self.head_barTank_frame_foot.pack()

        '''Заголовки Прогресс-Бара Танка'''
        self.label_headTank_top = Label(self.head_barTank_frame_top, text="100")
        self.label_headTank_middle = Label(self.head_barTank_frame_middle, text="50")
        self.label_headTank_foot = Label(self.head_barTank_frame_foot, text="0")

        self.label_headTank_top.pack()
        self.label_headTank_middle.pack(ipady=self.hightBar-258)
        self.label_headTank_foot.pack()

        '''Заголовки для названий Progress-линий'''
        self.label_progB_Tank = Label(self.head_Tank, text='Танк', padx=0)
        self.label_progB_BoreHole = Label(self.head_BoreHole, text='Скважина', padx=0)

        self.label_progB_Tank.pack(side=LEFT, anchor=W)
        self.label_progB_BoreHole.pack()


        #self.label_info = Label(self.heading_frame, text="Progress Bar Update Example")
        #self.label_info.pack()

        '''Установки для Progess_Bars'''
        self.progress_Tank = ttk.Progressbar(self.barTank_frame,
                                             orient="vertical",
                                             value=self.reainsTank,
                                             length=self.hightBar,
                                             maximum=self.vTank,
                                             mode='determinate')

        self.progress_BoreHole = ttk.Progressbar(self.barBoreHole_frame,
                                                 orient="vertical",
                                                 value=self.vBoreHole,
                                                 length=self.hightBar,
                                                 maximum=self.vBoreHole,
                                                 mode='determinate')

        self.progress_Tank.pack()
        self.progress_BoreHole.pack()



        '''Технические Wigets'''
        self.label = Label(self.data_frame,text="0")
        self.btn = Button(self.data_frame, text='On', command=self.switch_between)
        self.btn1 = Button(self.data_frame, text='Танк', command=self.switch_use_tank)



        #self.label.pack()
        #self.btn.pack()
        #self.btn1.pack(side=LEFT)



        #print(self.pogress_frame.winfo_height())


    def  use_tank_bar(self): #прогрессбар расхода танка
        self.progress_Tank['value'] -= self.speedTankPump /60 #Значение 60 для секунд
        self.label.config(text=int(self.progress_Tank['value']))
        if self.progress_Tank['value'] <= 0 :
            print('Емкость пуста!')
            self.flag_FullTank = False
        if  self.progress_Tank['value'] >=0:
            self.timer_3 = self.data_frame.after(100, self.use_tank_bar)  # реально ставить 1000
        else:
            print('Емкость пуста! Расход не возможен!')
            self.reainsTank = 0
            self.stop_use_tank_bar()

    def stop_use_tank_bar(self):
        print('timer3 off')
        self.data_frame.after_cancel(self.timer_3)

    def switch_use_tank(self): # переключатель расхода танка
        if self.flag_use_tank == False:
            self.flag_use_tank = True
            print('Start Use Tank')
            self.set_remais_tank()
            self.use_tank_bar()
        else:
            self.flag_use_tank =False
            print('Stop Use Tank')
            self.stop_use_tank_bar()
            self.remains_update()

    def start_Pump(self):
        pass

    def stop_Pump(self):
        pass


    def switch_between(self): # Переключатель для работы в тестовом режиме
        if self.flag_on_off == False:
            self.flag_on_off = True
            #print('On')
            self.btn.config(text='Off')
            self.set_remais_tank()
            self.up_prog_bar() # Запуск метода работы progress bar
            #print('tttt'+str(self.flag_FullTank))
        else:
            self.flag_on_off = False
            #print('Off')
            self.btn.config(text='On')
            self.stop_progerss_bar() # Остановка метода работы progress bar
            self.remains_update()
            self.recover_BoreHole()





    def up_prog_bar(self): # Метод работы progress bar
        self.progress_Tank['value'] += self.speedPump / 60 # Значение 60 для секунд
        self.label.config(text=int(self.progress_Tank['value']))
        self.progress_BoreHole['value'] -= self.speedPump / 60
        if self.progress_Tank['value'] >= self.vTank:
           self.flag_FullTank = True
           self.infoMsg.setMsg('Насос Выключен! Полный Танк!')
           self.connect.publish("hello/world", 'stop')


        if self.progress_Tank['value'] < self.vTank and self.progress_BoreHole['value'] > 0 and self.flag_FullTank == False:
            self.timer_1 = self.data_frame.after(100, self.up_prog_bar)  # реально ставить 1000

        elif self.flag_FullTank:
            self.infoMsg.setMsg('from prog Насос Выключен! Полный Танк!')
            self.connect.publish("hello/world", 'stop')
            self.stop_progerss_bar()
            self.recover_BoreHole()

        else:
            self.infoMsg.setMsg('Насос Выключен! Восстановление скважены!')
            self.connect.publish("hello/world", 'stop')
            self.stop_progerss_bar()
            self.recover_BoreHole()

    def test_prog(self): # Удалить
        self.infoMsg.setMsg('Насос Включен!')
        self.connect.publish("hello/world", 'start')
        self.up_prog_bar()

    def recover_BoreHole(self): # Метод работы progress bar восстановления скважены
        self.progress_BoreHole['value'] += self.speed_Rec_BH/60 # Значение 60 для секунд
        if self.progress_BoreHole['value'] < self.vBoreHole:
            self.timer_2 = self.data_frame.after(100, self.recover_BoreHole)

        else:
             self.stop_progress_BoreHole()
             if self.flag_FullTank == False and self.flag_on_off == True:
                self.infoMsg.setMsg('Насос Включен!')
                self.connect.publish("hello/world", 'start')
                self.up_prog_bar()


    def stop_progress_BoreHole(self):
        self.data_frame.after_cancel(self.timer_2)

    def fullTank(self):
        if self.progress_Tank['value'] >= self.vTank:
            self.flag_FullTank = True
            #print("изначально Полный танк!!!")
            #print(self.flag_FullTank)


    def stop_progerss_bar(self):
        self.connect.publish("hello/world", 'stop')
        self.data_frame.after_cancel(self.timer_1)

    def remains_update(self):
        self.reainsTank = self.progress_Tank['value']

    def set_remais_tank(self):
        self.progress_Tank['value'] = self.reainsTank

    def getFullTank(self):
        return self.flag_FullTank

    def setFlagOnOff(self, flag):
        self.flag_on_off = flag

    def getFlagOnOff(self):
        return self.flag_on_off





