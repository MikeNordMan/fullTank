import tkinter
from tkinter import *
from tkinter import ttk


''' 
root = Tk()
root.title('My test')
root.geometry('350x300')

frame_1 = Frame(borderwidth=1, relief=SOLID, pady=5, padx=10)
frame_1.pack(pady=1)

frame_2 = Frame(borderwidth=1, relief=SOLID, pady=5, padx=10)
frame_2.pack(pady=1)



label_1 =Label(frame_1, text="Первый блок", padx=(325-78)/2, pady=20) # 78
label_1.pack()

label_2 =Label(frame_2, text="Второй блок", padx=(325-74)/2, pady=20) # 74
label_2.pack()



label_2.update()
print(label_2.winfo_width())  # Возвращает ширину виджета использовать только с update





root.mainloop()

'''

''' Тоже, но через классы. Все получилось!!!'''

class Frame_1(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.frame = Frame(borderwidth=1, relief=SOLID, pady=5, padx=10)
        self.label_1 = Label(self.frame, text="Первый блок", padx=(325-78)/2, pady=20)
        self.frame.pack(pady=1)
        self.label_1.pack()

class Frame_2(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.frame = Frame(borderwidth=1, relief=SOLID, pady=5, padx=10)
        self.label_1 = Label(self.frame, text="Второй блок", padx=(325-74)/2, pady=20)
        self.frame.pack(pady=1)
        self.label_1.pack()

        self.label_1.update()
        print(self.label_1.winfo_width())


class Frame_3(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.frame = Frame(borderwidth=1, relief=SOLID, pady=5, padx=10)
        self.label_1 = Label(self.frame, text="Третий блок", padx=(325-72)/2, pady=20)

        self.frame.pack(pady=1)
        self.label_1.pack()

        self.frame.update()
        print(self.frame.winfo_width())


class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Test my App")
        self.geometry('350x300')

        self.frame_a = Frame_1(self)
        self.frame_b = Frame_2(self)
        self.frame_c = Frame_3(self)




app = App()
app.mainloop()


