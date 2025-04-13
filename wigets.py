import tkinter
from tkinter import *

class infoPart(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.frame_collor = None
        self.msg = '   Тут сообщение   '
        self.frame = Frame(width=350, height=50, borderwidth=1, relief=SOLID, pady=5, padx=10)
        #self.label_1 = Label(self.frame, text="Первый блок", padx=(325-78)/2, pady=20)
        self.infoLabel = Label(self.frame, text=self.msg, padx=1, pady=1)
        #self.infoLabel = Label(self.frame, padx=2, pady=2)


        self.frame.pack(fill=X, padx=2, pady= 1)
        #self.frame.config(width=300, height=50)
        #self.label_1.pack()
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


class AnalogRun(tkinter.Frame):
    def __init__(self, master, infoMsg):
        super().__init__(master)
        self.infoMsg = infoMsg

        self.flag_btn = True
        self.flag_timer = True
        self.flag_msg_1 = True
        self.flag_msg_2 = True
        self.timer_id = None

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
        self.fill_Create()


    def on_off(self):
        if self.flag_btn == True:
           self.pumpON()
           self.timeRun(self.count, self.min)

        else :
           self.pumpOff()

    def pumpON(self):
        self.infoMsg.setMsg('Насос Включен!')
        self.fill_Destroy()
        self.flag_timer =True
        self.wigetTimerCreate()
        self.org_color = self.btn.cget('bg')
        self.btn.config(text="Stop", bg='red')
        self.flag_btn = False

    def wigetTimerCreate(self):
        self.label_timer = Label(self.timer_frame, text='00:00')
        self.label_timer.pack()

    def fill_Create(self):
        self.label_fill = Label(self.timer_frame, text='Время работы 5 мин')
        self.label_fill.pack()

    def fill_Destroy(self):
        self.label_fill.destroy()

    def pumpOff(self):
        self.infoMsg.setMsg('Тут сообщение')
        print('Stop')
        self.btn.config(text="Start", bg=self.org_color)
        self.flag_btn = True
        self.flag_timer = False
        self.count = 0
        self.min = 0
        self.timer_frame.after_cancel(self.timer_id)
        self.label_timer.destroy()
        self.fill_Create()


    def msg_controll(self, min):
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