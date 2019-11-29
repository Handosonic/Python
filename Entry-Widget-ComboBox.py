from tkinter import *
from PIL import Image,ImageTk
import my_color
import sys
import codecs 
color1 = my_color.colors
#----------------------TEXT----------------
#path = 'D:/Final/Final/data.txt' ;	data_file = open(path,'w')


  
root = Tk()
root.geometry('400x400')
root.title("Иргэний бүртгэл")
root.resizable(0,0)  # хүрээний хэмжээг өөрчлөхгүй болгож байна
#---------------------IMAGE---------------------------
img = Image.open("10302.png"); img = img.resize((80,80),resample = 1)
photo= ImageTk.PhotoImage(img)
lab = Label(image=photo)
lab.pack( pady=(15))

#----------------------MENU------------------------------

menubar = Menu(root)
'''
menu = Menu(menubar, tearoff=0)
menu.add_command(label=" Бүртгэх   /register/", command=menuClicked)
menu.add_command(label=" Засварлах     /edit/", command=menuClicked)
menu.add_command(label=" Устгах      /delete/", command=menuClicked)
menu.add_separator()
menu.add_command(label=" Гарах      ", command=root.quit)
menubar.add_cascade(label="Цэс", menu=menu)
menubar.add_cascade(label="About")
'''

label1 = Label(root,text="Цэргийн бүртгэл",relief="flat", width=19, bg=color1["fuchsia"], font=("Consolas",15,""))
label1.place(x=89,y=113)
name = StringVar()
label2 = Label(root,text="Нэвтрэх нэр: ", width=19, font=("Consolas",13,"bold"))
label2.place(x=58,y=180)
entry1 = Entry(root, textvar=name)
entry1.place(x=220,y=183)

fath_name = StringVar()
label3 = Label(root,text="Нууц үг: ", width=19, font=("Consolas",13,"bold"))
label3.place(x=40,y=220)
entry1 = Entry(root, textvar=fath_name)
entry1.place(x=220,y=223)

#label3 = Label(root,text="Аймаг хот: ", width=19, font=("Consolas",11,"bold"))
#label3.place(x=50,y=255)

#hot = StringVar()
#list1 = ['murun','tosontsengel','zawxan']
#droplist=OptionMenu(root,hot,*list1)
#hot.set("Сонгох...")
#droplist.config(width=15)
#droplist.place(x=194,y=255)

def printt():
	first=name.get()
	sec=fath_name.get()
	print(first,sec)
	#path = 'D:/Final/Final/data.txt' 
	#data_file = codecs.open(path, 'a','utf8') #w шинээр үүсгэж бичнэ
	#data_file.write(first)


b1 = Button(root,text="Login",width=12,bg='brown',fg='white',command=printt)
b1.place(x=80,y=300)
b2 = Button(root,text="Exit",width=12,bg='brown',fg='white',command=exitt)
b2.place(x=230,y=300)

root.config(menu=menubar)

root.mainloop()


