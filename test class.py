''' Тут тестировать несколько блоков wigets ТОЛЬКО!!!'''
import threading
from multiprocessing import Process

import tkinter
from wigets import *
from tkinter import *
from settingViget import *
from progress_tank import *
from commun_Server import ComRaspbery

class App(tkinter.Tk):

    def __init__(self):
        super().__init__()
        self.title("Test new Frame")
        self.geometry('650x700')


        self.bildFrame()
        print('Построение закончено')

        '''Тут код программы'''
        #self.con = ComRaspbery(self.info_bl)
        self.con.runConnect()



    def bildFrame(self):


        '''Инициализация Фреймов'''
        self.main_frame = tkinter.Frame()

        self.header_fr = Frame(self.main_frame, borderwidth=1, relief=SOLID, pady=5, padx=5)

        self.body_fr = Frame(self.main_frame, borderwidth=1, relief=SOLID, pady=5, padx=5)

        self.body_fr_Left = Frame(self.body_fr, borderwidth=1, relief=SOLID, pady=5, padx=5)
        self.body_fr_Right = Frame(self.body_fr, borderwidth=1, relief=SOLID, pady=5, padx=5)

        self.foot_fr = Frame(self.main_frame, borderwidth=1, relief=SOLID, pady=5, padx=5)

        '''Вот Здесь создовать экземпляры классов блоков-Wiggets'''


        self.info_blok = InfoPart(self.header_fr) # Создание инормационного блока
        self.info_blok.bildFrame()

        self.con = ComRaspbery(self.info_blok) # Создание экземпляра для связи


        self.test_bar = Progress_Tank(self.body_fr_Right, self.info_blok, self.con)

        self.test_b2 = TestW(self.foot_fr) # Тестовый блок (Удалить)

        self.test_bl = TestW(self.body_fr_Left) # Тестовый блок (Удалить)

        self.analog = AnalogRun(self.body_fr_Left, self.info_blok, self.test_bar)



        '''Отрисовка Фреймов'''

        self.main_frame.pack(fill=X)
        self.header_fr.pack(fill=X)

        self.body_fr.pack(fill=X)
        self.body_fr_Left.pack(side=LEFT, fill=X)
        self.body_fr_Right.pack(anchor=E)

        self.foot_fr.pack(fill=X)




        #self.labA.pack()
        #self.labB.pack()

        #self.frame_a = infoPart(self)
        #self.pogress = Progress_Tank(self, self.frame_a)
        #self.aRun = AnalogRun(self, self.frame_a, self.pogress)

        #self.pogress.update_progress_bar()



def startWigets():
    app = App()
    #con = ComRaspbery()
    #con.runConnect()
    app.mainloop()

def startConnect():
    #con =ComRaspbery(self.info_bl)
    #con.runConnect()
    pass


def main():
        startWigets()


if __name__ == '__main__':
    main()
