import tkinter
from tkinter import *
#from tkinter import ttk

class InfoPart(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.msg = 'test'
        self.frame = Frame(borderwidth=1, relief=SOLID, width = 150, height = 150, pady=5, padx=10) # Высота не используется
        #self.widthInfo = Label(self.frame)
        self.infoMessage =Label(self.frame, text=self.msg, padx=5)
        
        #self.msg = 'test'
        
        self.frame.pack(fill="both", side="top", expand=True)
        #self.frame.pack(fill="y", side="top", expand=True) Настроить по высоте (как то) 
        #self.widthInfo.pack()
        self.infoMessage.pack()
        
    def setMsg(self, msg):
        self.msg = msg
        self.infoMessage.config(text = msg)
        #self.infoMessage.set(msg)

'''Класс принудительного включениея насоса'''

class PumpOnAnalog(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.main_frame = Frame(borderwidth=1, relief=SOLID, pady=5, padx=5) # основной Frame
        self.frame_btn = Frame(self.main_frame, borderwidth=1, relief=SOLID, pady=5, padx=5)
        self.frame_tCl = Frame(self.main_frame, borderwidth=1, relief=SOLID, pady=5, padx=5)
        
        self.btn_on = Button(self.frame_btn, text='Power On', command= self.power_on)
        self.timer =Label(self.frame_tCl, text='New Timer')
        
        self.main_frame.pack()
        self.frame_btn.pack(side=LEFT)
        self.frame_tCl.pack()
        
        self.btn_on.pack()
        self.timer.pack()
        
    def power_on(self):
        print('On')
        
        
        
        
        