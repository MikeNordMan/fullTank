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
        self.btnNew = Button(self.frame, text='New Block', command= self.newBlock)
        
        self.frame.pack(pady=1)
        self.label_1.pack()
        self.btnNew.pack()
        
        self.label_1.update()
        print(self.label_1.winfo_width())
        
    def newBlock(self):
         self.a = Frame_3(self.frame)
         print('test')


class Frame_3(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.frame = Frame(borderwidth=1, relief=SOLID, pady=5, padx=10)
        self.label_1 = Label(self.frame, text="Третий блок", padx=(325-72)/2, pady=20)
        
        self.frame_info = Frame(self.frame, pady=5, padx=10)
        
        self.lab_info = Label(self.frame_info, text='Инфо')
        self.btnCreate = Button(self.frame_info, text='Create')
        self.btnDel = Button(self.frame_info, text='Delite')

        self.frame.pack(pady=1)
        self.label_1.pack()
        self.frame_info.pack()
        self.lab_info.pack(side=LEFT)
        self.btnCreate.pack(side=LEFT)
        self.btnDel.pack(side=LEFT)
        self.frame.update()
        print(self.frame.winfo_width())


class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Test my App")
        #self.geometry('350x300')

        self.frame_a = Frame_1(self)
        self.frame_b = Frame_2(self)
        self.frame_c = Frame_3(self)




app = App()
app.mainloop()
