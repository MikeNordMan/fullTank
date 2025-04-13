import tkinter
from tkinter import *
from wigets import *
class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Test my App")
        #self.geometry('350x300')

        self.frame_a = infoPart(self)
        #self.frame_a.setMsg('test')
        self.frame_b = Frame_2(self, self.frame_a)
        self.aRun = AnalogRun(self, self.frame_a)




def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()


