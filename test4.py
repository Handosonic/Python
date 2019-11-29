from tkinter import *
from tkinter.ttk import *
scr = Tk()
scr.title("Combobox - Tkinter Widgets")
scr.geometry('300x100')
def select():
    value = "Value: " + combo.get()
    label.config(text = value)
    
combo = Combobox(scr, values=[ "Python", "PHP", "HTML", "MySQL", "C++", "OUT"])
combo.current(0)
combo.pack()
button = Button(scr, text="Select", command=select)
button.pack()
label = Label(scr)
label.pack()
scr.mainloop()