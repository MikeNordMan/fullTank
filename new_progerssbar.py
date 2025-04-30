import tkinter as tk
from tkinter import ttk

tankMax = 2500  # объем танка
speedPump = 12  #скорость работы насоса л в минуту
flag = False


def update_progress_bar():
        progress_bar['value'] += speedPump/60
        #print(int(progress_bar['value']))
        label.config(text=int(progress_bar['value']))
        if progress_bar['value'] < tankMax:
            window.after(100, update_progress_bar) # реально ставить 1000




window = tk.Tk()
window.title("Progress Bar Update Example")

progress_bar = ttk.Progressbar(window, length=200, mode='determinate')
progress_bar.pack()

label = tk.Label(text="0")
label.pack()
btn = tk.Button(text='Start', command=changeF)
btn.pack()

update_progress_bar()

window.mainloop()