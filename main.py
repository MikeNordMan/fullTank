import tkinter as tk
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("200x300")


def printVal():
    print()


def clear():
    entry_1.delete(0, END)  # удаление введенного текста


def getData():
    a = entry_1.get()  # получение введенного текста
    print(a)
    return a


def setData():
    label['text'] = getData()


def btnClik():
   setData()
   clear()






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

