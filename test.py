# importing tkinter 
from tkinter import * 
from tkinter import ttk 
from tkinter.messagebox import askyesno 
 
root = Tk() 
 
root.geometry('200x100') 
   
input_text = StringVar() 
  
entry1 = ttk.Entry(root, textvariable = input_text, justify = CENTER) 
  
entry1.focus_force() 
entry1.pack(side = TOP, ipadx = 30, ipady = 2) 
  
save = ttk.Button(root, text = 'Save', command = lambda : askyesno( 
                                'Confirm', 'Do you want to save?')) 
save.pack(side = TOP, pady = 10) 
  
root.mainloop()