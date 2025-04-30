import tkinter
from tkinter import *
from progress_tank import *

class infoPart(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.frame_collor = None
        self.msg = '   Тут сообщение   '
        self.frame = Frame(width=350, height=50, borderwidth=1, relief=SOLID, pady=5, padx=10)
        self.label_1 = Label(self.frame, text="Первый блок", padx=(325-78)/2, pady=20)
        self.infoLabel = Label(self.frame, text=self.msg, padx=1, pady=1)
        #self.infoLabel = Label(self.frame, padx=2, pady=2)


        self.frame.pack(fill=X, padx=2, pady= 1)
        #self.frame.config(width=300, height=50)
        self.label_1.pack(side=LEFT)
        self.infoLabel.pack(padx=2)
        self.getCollor()

    def setMsg(self, text):
        self.msg = text
        self.infoLabel.config(text=self.msg)

    def getCollor(self):
        self.frame_collor = self.infoLabel.cget('bg')

    def setCollorBg(self, collor):
        self.infoLabel.config(bg=collor)


class Frame_2(tkinter.Frame):
    def __init__(self, master, infoMsg):
        super().__init__(master)
        self.infoMsg = infoMsg
        self.frame = Frame(borderwidth=1, relief=SOLID, pady=5, padx=10)
        self.label_1 = Label(self.frame, text="Второй блок", padx=(325-74)/2, pady=20)
        self.btn = Button(self.frame, text="Test", command=self.setInfo)

        self.frame.pack(fill=X, padx=2, pady= 1)
        self.label_1.pack()
        self.btn.pack()

        self.label_1.update()
        print(self.label_1.winfo_width())

    def setInfo(self):
        msg = 'Новое сообщение Новое сообщение Новое сообщение Новое сообщение Новое сообщение '
        self.infoMsg.setMsg(msg)

'''___________________________________________________________________________'''
class AnalogRun(tkinter.Frame):
    def __init__(self, master, infoMsg, bar):
        super().__init__(master)
        self.infoMsg = infoMsg
        self.bar = bar


        self.flag_btn = True
        self.flag_timer = True
        self.flag_msg_1 = True
        self.flag_msg_2 = True
        self.timer_test = None

        self.org_color = None

        self.ms = 300
        self.minMax = 5
        self.minMidl = 3
        self.count = 0
        self.min = 0

        self.main_frame = Frame(borderwidth=1, relief=SOLID, pady=5, padx=5)

        self.btn_frame = Frame(self.main_frame, borderwidth=1, relief=SOLID, pady=5, padx=5)
        self.timer_frame = Frame(self.main_frame, borderwidth=1, relief=SOLID, pady=5, padx=5)

        self.btn = Button(self.btn_frame, text='Start', command=self.on_off)


        self.main_frame.pack(fill=X, padx=2, pady= 1)
        self.btn_frame.pack(side=LEFT)
        self.timer_frame.pack()
        self.btn.pack()
        self.wigetLabelCreate()


    def on_off(self):
        #print(self.bar.getFullTank())

        if self.bar.getFullTank()== False:
            if self.bar.getFlagOnOff() == False:
                self.btn_Start()
                self.bar.setFlagOnOff(True)
                self.bar.set_remais_tank()
                self.bar.up_prog_bar()  # Запуск метода работы progress bar
                self.infoMsg.setMsg('Насос Включен!')
                #self.bar.test_prog()
                self.fullTank_check() #Запуск отслеживания полного Танка
            else:
                self.bar.setFlagOnOff(False)
                self.infoMsg.setMsg('Насос Выключен!')
                self.flag_btn = True
                self.btn_Stop()
                self.bar.stop_progerss_bar()  # Остановка метода работы progress bar
                self.bar.remains_update()
                self.bar.recover_BoreHole()
                self.fullTank_check_stop()  # Остановка отслеживания полного Танка
        else:
            #self.infoMsg.setMsg('from wig Насос Выключен! Полный Танк!')
            self.btn_Stop()
            self.fullTank()

    def btn_Start(self):
        #self.infoMsg.setMsg('Насос Включен!')
        self.org_color = self.btn.cget('bg')
        self.btn.config(text="Stop", bg='red')
        self.label_timer.config(text='Ручной Режим Активирован!')
        self.flag_btn = False

    def wigetLabelCreate(self):
        self.label_timer = Label(self.timer_frame, text='Активация ручного режима')
        self.label_timer.pack()

    def fill_Destroy(self):
        self.label_fill.destroy()

    def btn_Stop(self):
        #self.infoMsg.setMsg('')
        #print('Stop  from App')
        self.btn.config(text="Start", bg=self.org_color)
        self.label_timer.config(text='Ручной Режим Деактивирован!')
        self.flag_btn = True

    def fullTank(self):
        self.infoMsg.setMsg('Внимание! Полный Танк!')

    def fullTank_check(self):
        fullTank = self.bar.getFullTank()
        if fullTank == False:
            self.timer_test = self.btn_frame.after(100, self.fullTank_check)
        else:
            #print('else rul')
            self.fullTank_check_stop()
            self.infoMsg.setMsg('Насос Выключен! Полный Танк!')
            self.btn_Stop()

    def fullTank_check_stop(self):
         self.btn_frame.after_cancel(self.timer_test)
         print("stop timer")






    def msg_controll(self, min): # Удалить
        if min >= self.minMidl and self.flag_msg_1:
            self.infoMsg.setMsg('Внимание! Время работы насоса 3 минуты')
            self.infoMsg.setCollorBg('yellow')

            self.flag_msg_1 = False
        if min >= self.minMax and self.flag_msg_2:
            self.infoMsg.setMsg('Внимание! Насос выключен требуется восстановление скважны')
            self.infoMsg.setCollorBg(self.infoMsg.frame_collor)
            print('Stop')
            self.flag_msg_2 = False
            self.flag_timer = False
            #self.pumpOff()

    def timeRun(self, count, minute):
        if self.flag_timer:
            sec = str(count)
            if count < 10:
                sec = '0' + sec

            if count > 19:
                minute = minute + 1
                sec = '00'
                count= 0
            self.msg_controll(minute)

            self.label_timer.config(text='0' + str(minute) + ':' + sec)

        self.timer_id = self.timer_frame.after(self.ms, self.timeRun, count + 1, minute)

'''____________________________________________________________________________________________________'''


class A():
    def __init__(self):
        self.a = 100

    def get_a(self):
        return self.a
    def set_a(self, new):
        self.a = new

class B():
    def __init__(self, cl):

        self.b = 'tt'
        self.cl = cl

    def get_b(self):
        return self.cl.get_a()

    def set_b(self, new):
        self.cl.set_a(new)