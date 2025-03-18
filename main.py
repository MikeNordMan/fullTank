import tkinter as tk
from tkinter import *
from tkinter import ttk
from with_Sript import MyScript

root = Tk()
root.geometry("200x300")
tl = []

def printVal():
    print()


def clear():
    entry_1.delete(0, END)  # удаление введенного текста
    entry_2.delete(0, END)
    entry_3.delete(0, END)


def getData():
    n = []
    a = entry_1.get()  # получение введенного текста
    n.append(a)
    b = entry_2.get()
    n.append(b)
    c = entry_3.get()
    n.append(c) 
    #print(n[0] + n[1] + n[2])
    #a = n[0] + n[1] + n[2]
    #print(a)
    return n


def setData(mylist, tl):
    a = mylist[0]
    b = mylist[1]
    c = mylist[2]
    #print(a)
    label['text'] = a +'\n'+ b + '\n'+ c
    a = MyScript(a,b,c)
    tl.append(a)


def btnClik():
   setData(getData(),tl)
   clear()
   print(tl) 





entry_1 = tk.Entry()
entry_1.pack(anchor=N,)
entry_2 = tk.Entry()
entry_2.pack(anchor=N)
entry_3 = tk.Entry()
entry_3.pack(anchor=N)

btn = tk.Button(text="Click", command=btnClik)
btn.pack(anchor=N)

label = tk.Label(text="Пример:")
label.pack(anchor=N)




if __name__ == '__main__':
    root.mainloop()
