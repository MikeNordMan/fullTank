from wigets import *
from tkinter import *
#global timer_id
class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        #self.timer_id = timer_id
        self.title("Test new Frame")
        #self.geometry('350x300')

        #self.frame_a = infoPart(self)
        #self.frame_a.setMsg('test')
        #self.frame_b = Frame_2(self, self.frame_a)
        #self.frame_c = Frame_3(self)
        self.aRun = AnalogRun(self)


def main():
        app = App()
        app.mainloop()


if __name__ == '__main__':
    main()
