from tkinter import *
from tkinter.ttk import *

root=Tk()
root.title('aying7.com')

style = Style()
style.theme_use('default')
# Self test for each subject,'winnative','clam','alt','default','classic' Test successful.
# windows theme:('winnative','clam','alt','default','classic','vista','xpnative')

style.configure("my.Horizontal.TProgressbar",  background='lightblue') #troughcolor ='blue',
style.configure("2.Horizontal.TProgressbar", troughcolor ='red', background='yellow')
style.configure("3.Horizontal.TProgressbar", troughcolor ='black', background='red')
style.configure("4.Horizontal.TProgressbar", troughcolor ='white', background='lightblue')

val = IntVar(value=300)


P1 = Progressbar(root, style="my.Horizontal.TProgressbar",  length=180,value=100,  variable=val)
P1.pack(padx=10,pady=5)
label = Label(textvariable=val)
label.pack(anchor=NW, padx=6, pady=6)


P1.start(100)



P2 = Progressbar(root,style="2.Horizontal.TProgressbar",length=180)
P2.pack(padx=10,pady=5)
P2.start()

P3 = Progressbar(root,style="3.Horizontal.TProgressbar",length=180)
P3.pack(padx=10,pady=5)
P3.start()

P4 = Progressbar(root,style="4.Horizontal.TProgressbar",length=180)
P4.pack(padx=10,pady=5)
P4.start()

root.mainloop()