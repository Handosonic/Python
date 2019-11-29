# importing tkinter 
from tkinter import * 
from tkinter import ttk 

 
root = Tk() 
 
root.geometry('300x200') 
   
input_text = StringVar() 
  
entry1 = ttk.Entry(root, textvariable = input_text, justify = CENTER) 
  
entry1.focus_force() 
entry1.pack(side = TOP, ipadx = 1, ipady = 2)
  
save = ttk.Button(root, text = 'Save', command = lambda : askyesno( 
                                'Confirm', 'Do you want to save?')) 
save.pack(side = TOP, pady = 10) 
  
root.mainloop()