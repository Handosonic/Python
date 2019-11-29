import gspread 
from password_encrypt import encrypt_pass
from graphic import login_pass
from tkinter import messagebox
from oauth2client.service_account import ServiceAccountCredentials

#def add_member(name,password):
	#sheet.append_row([name, password])
class get_login_information():
	def __init__(self):

		self.scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
		self.creds = ServiceAccountCredentials.from_json_keyfile_name('527216736c6c.json',self.scope)
		self.client = gspread.authorize(self.creds)

		self.sheet = self.client.open('Soldier_Password_Data').sheet1

		self.soldiers = self.sheet.get_all_records()	
		#sheet = client.close('Soldier_Password_Data').sheet1
	def data_return(self):
		return self.soldiers

	def data_update(self, name, new_password):
		name = name
		new_password = new_password
		Encod_v1 = encrypt_pass(new_password)
		Encod_v2 = Encod_v1.enco()
		Encoded_password = Encod_v1.encrypt_passv2(Encod_v2)
		print(name, new_password)
		for i in range(len(self.soldiers)):
			if(self.soldiers[i].get('Real_Name') == name):
				print(i , self.soldiers[i].get('Name'))
				self.sheet.update_cell(i+2,2,Encoded_password)
				print('password changed')
				messagebox.showinfo("Completed", "Амжилттай солигдлоо")
				break
	#def add_member(self, real_name, login_name, password, level):
