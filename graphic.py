from tkinter import *
from PIL import Image,ImageTk
import my_color
import sys
import codecs
from password_encrypt import encrypt_pass
color1 = my_color.colors
from tkinter import messagebox

#---sheetnees мэдээлэлээ татаж байна


class login_pass():	
	def __init__(self, data, usr):
		self.usr = usr
		self.login_attempt = False
		self.data = data
	#def data(self):
		
	def login(self):
		self.root = Tk()
		self.root.geometry('400x420')
		self.root.title("Цэргийн бүртгэл")
		self.root.resizable(0,0)  # хүрээний хэмжээг өөрчлөхгүй болгож байна
	#---------------------IMAGE---------------------------
		img = Image.open("10302.png"); img = img.resize((80,80),resample = 1)
		photo= ImageTk.PhotoImage(img)
		lab = Label(image=photo)
		lab.pack(pady=(15))
	
	#----------------------MENU------------------------------
		label1 = Label(self.root,text="Цэргийн бүртгэл",relief="flat", width=19, bg=color1["fuchsia"], font=("Consolas",15,""))
		label1.place(x=89,y=113)
		
		self.name = StringVar()
		self.password = StringVar()

		label2 = Label(self.root, text="Нэвтрэх нэр: ", width=19, font=("Consolas",13,"bold"))
		label2.place(x=58,y=180)
		entry1 = Entry(self.root, textvar = self.name)
		entry1.place(x=220,y=183)
			
		label3 = Label(self.root,text="Нууц үг: ", width=19, font=("Consolas",13,"bold"))
		label3.place(x=40,y=220)
		entry1 = Entry(self.root, textvar= self.password , show='*')
		entry1.place(x=220,y=223)

		def exitt():
			exit()
		#def quit1(root):
    		#root.quit()
    
		b1 = Button(self.root,text="Login",width=12,bg='brown',fg='white',command=self.hariu)
		b1.place(x=80,y=300)
		b2 = Button(self.root,text="Exit",width=12,bg='brown', fg='white',command=exitt)#root.quit
		b2.place(x=230,y=300)

		self.root.mainloop()
		

	#@staticmethod
	#def hariu(self):
	#	print('zaazoo')
	#	return name

	def hariu(self):
		name = self.name.get()
		password = self.password.get()
		length = len(self.data)
		#print('name:',name); print('pass:',password)
		q = 0
		for i in range(length):
			if(self.data[i].get('Name') == name):
				#print('name taarch bna')
				self.Decod = encrypt_pass(str(self.data[i].get('Pass')))
				Decode_v1 = self.Decod.deco()
				self.Decoded_password = self.Decod.deco_v2()
				if(self.Decoded_password == str(password)):
					print('OK PASS')
					self.usr[0] = self.data[i].get('Real_Name')
					#self.password[0] = self.data[i].get('Pass')
					self.usr[1] = self.data[i].get('Level')
					self.usr[2] = 1
					#self.root.quit()
					self.root.destroy()
					q = 1
					break
				else:
					self.msg_box()
					q = 1
			else:
				if(q is 0 and i is length-1):
					q = 1
					self.msg_box_alert()

	def msg_box(self):
		messagebox.showwarning("Алдаа", "Нэвтрэх нууц үг буруу байна")
	def msg_box_alert(self):
		messagebox.showwarning("Алдаа", "Нэвтрэх нэр болон нууц үг буруу байна")	

class duud:
	def __init__(self):
		self.b = 1 

	def area(self):
		if(self.b is 1):
			print('b is 1')
			return self.bytsaalt()

	@staticmethod		
	def bytsaalt():
		return 'zazooo'