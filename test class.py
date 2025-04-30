import tkinter
from wigets import *
from tkinter import *
from settingViget import *
from progress_tank import *
#global timer_id
class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        #self.timer_id = timer_id
        self.title("Test new Frame")
        #self.geometry('350x300')

        self.frame_a = infoPart(self)
        self.pogress = Progress_Tank(self, self.frame_a)
        self.aRun = AnalogRun(self, self.frame_a, self.pogress)

        #self.pogress.update_progress_bar()







def main():
        app = App()
        app.mainloop()


if __name__ == '__main__':
    main()
