from tkinter import *
from tkinter.ttk import Combobox
from PIL import Image,ImageTk
from password_encrypt import encrypt_pass
from tkinter import messagebox
from login_data import get_login_information
from password_encrypt import check_password
from settings import Settings

se = Settings()

def donoting():
    pass
class main_page():
    def __init__(self, setting, user, data):
        self.sheet_information = data
        self.user_info = user
        self.set = setting
        self.root2 = Tk()
        resolution = self.set.main_menu_width +'x'+ self.set.main_menu_length
        self.root2.geometry(resolution)
        self.length = len(self.sheet_information)
        self.root2.title("Үндсэн хуудас")
        self.root2.resizable(0,0)
        print(self.user_info)
        self.menubar = Menu(self.root2)
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="Нууц үг солих", command = self.change_password)
        if(self.user_info[1] == 'admin'):
            filemenu.add_command(label="Шинээр эрх үүсгэх", command = self.new_member_create)
        filemenu.add_separator()
        filemenu.add_command(label="Гарах", command=self.root2.quit)
        self.menubar.add_cascade(label="Цэс", menu=filemenu)
        

        help1 = Menu(self.menubar, tearoff=0)
        help1.add_command(label="Бидний тухай", command=donoting)
        self.menubar.add_cascade(label="About", menu=help1)
        

        self.root2.config(menu=self.menubar)
        self.root2.mainloop()
#-----------------------------------------------------------------#
    
    def change_password(self):
        self.root1 = Tk()
        self.root1.geometry('320x250')
        self.root1.title("Нууц үг солих хэсэг")
        self.root1.resizable(0,0)
        x = 0 ; x_grid = 0
        
        label1 = Label(self.root1,text="           Хуучин нууц үг : ", width=18,font=("Times",13)).grid(padx=x , row=0, column = 0, pady = 14)
        self.old_pass = Entry(self.root1, relief = 'solid' , show = '*')
        self.old_pass.grid(ipady = 2 , row = 0 , column = 1,padx=x_grid, pady=14)
        
        label2 = Label(self.root1,text="              Шинэ нууц үг : ", width=18, font=("Times",13)).grid(padx = x, row=1, column = 0 , pady = 2)
        self.new_pass = Entry(self.root1, relief = 'solid', show = '*')
        self.new_pass.grid(ipady = 2, row = 1, column = 1,padx=x_grid , pady = 2)
      
        label3 = Label(self.root1,text="         Давтан бичнэ үү : ", width=16, font=("Times",13),borderwidth = '5').grid(padx=x, row=2, column=0, pady = 14)
        self.new_pass_Re = Entry(self.root1, relief ='solid' , show = '*')
        self.new_pass_Re.grid(ipady = 2, row = 2 , column = 1,padx=x_grid, pady=14)
        

        Towch1 = Button(self.root1, text="  Батлах  ", bg='#2B9DF6' , command=self.nuuts_ug, relief='flat' , font=('Consolas',13))
        #Towch1.grid(row = 4, column = 0, padx = 50) 
        Towch1.place(x=35,y=160)

        Towch2 = Button(self.root1,text="  Цуцлах  ", bg='#2B9DF6'  , command=self.exitt ,relief='flat' , font=('Consolas',13))
        #Towch2.grid(row=15, column=1)
        Towch2.place(x=185,y=160)
        self.root1.mainloop()
  

#--------------------------------------------------------------------#
    def exitt(self):
        self.root1.destroy()
    def nuuts_ug(self):
        old_pass = self.old_pass.get()
        new_pass = self.new_pass.get()
        new_pass_Re = self.new_pass_Re.get()
        Error = 0
        Collection = 0 # 2 нөхцөл биелсэн байх хэрэгтэй
        print(old_pass,new_pass,new_pass_Re)

        for i in range(self.length):
            #print('loop')
            sheet_name = self.sheet_information[i].get('Real_Name')
            if(sheet_name == self.user_info[0]):
                Decodv1 = encrypt_pass(str(self.sheet_information[i].get('Pass')))
                dd = Decodv1.deco()
                Decodv2 = Decodv1.deco_v2()
                if(str(old_pass) == Decodv2):
                    print('old_pass zow bna')
                    Collection += 1
                else:
                    Error += 1
        if not new_pass:
            Collection -=1
            messagebox.showwarning("Анхааруулга", "Шинэ нууц үг хоосон байна")
        if(new_pass == new_pass_Re):
            print('taarch bna')
            Collection +=1
        else:
            Error += 2
        if(Error > 0):
            if(Error is 1):
                messagebox.showwarning("Анхааруулга", "Хуучин нууц үг буруу байна")
            elif(Error is 2):
                messagebox.showwarning("Анхааруулга", "Шинэ нууц үг буруу байна")
            else:
                messagebox.showerror("Анхааруулга", "Бүгд буруу байна")
        if(Collection is 2):
            print('password solix heseg')  
            a = get_login_information()
            a.data_update(self.user_info[0] , new_pass)
        
    def new_member_create(self):
        self.rootmem = Tk()
        self.rootmem.geometry('620x420')
        self.rootmem.title('Шинээр хэрэглэгч бүртгэх хэсэг')
        self.rootmem.config(bg="skyblue")
        self.rootmem.resizable(0,0);  x = 5 ; x_grid = 0
        comment_color = '#686363'
        color = "skyblue"
        #label3 = Label(self.root1,text="         Давтан бичнэ үү : ", width=16, font=("Times",13),borderwidth = '5').grid(padx=x, row=2, column=0, pady = 14)
        Label(self.rootmem, text = "           Жинхэнэ нэр, овгийн үсэг :", width = 25, font=("Times",13), borderwidth = '5',bg=color).grid(padx=x, row=0, column=0,pady=20)
        self.real_name = Entry(self.rootmem , relief='solid', width=22)
        self.real_name.grid(padx=x_grid, ipady=2, row=0, column = 1, pady=20)

        Label(self.rootmem, text = "                     Нэвтрэх нэр /Англи/ :", width = 25, font=("Times",13), borderwidth = '5',bg=color).grid(padx=x, row=1, column=0)
        self.login_name = Entry(self.rootmem, relief='solid', width=22)
        self.login_name.grid(padx=x_grid,ipady=2, row=1, column = 1)
        
        Label(self.rootmem, text = "                               Шинэ Нууц үг :" ,  width = 25, font=("Times",13), borderwidth = '5',bg=color).grid(padx=x, pady=20, row=3, column=0)
        
        self.new_pass1 = Entry(self.rootmem, relief='solid' ,width=22 )
        self.new_pass1.grid(padx=x_grid, ipady=2, row=4, column=1, pady=20)
        
        Label(self.rootmem, text = "               Нууц үг Дахин оруулах :", width = 25, font=("Times",13), borderwidth = '5',bg=color).grid(padx=x, row=4, column=0,pady=20)

        Label(self.rootmem, text = "                       Хандалтын түвшин :", width = 25, font=("Times",13), borderwidth = '5',bg=color).grid(padx=x, row=2, column=0,pady=20)

        self.new_pass1_Re = Entry(self.rootmem, relief='solid', width=22)
        self.new_pass1_Re.grid(padx=x_grid, ipady=2, row=3, column=1 ,pady=20)    
        Label(self.rootmem, text = 'admin, user, clinder, darga, general' ,font=("Times",11), bg=color,fg=comment_color).place(x=310,y=100)

        Label(self.rootmem, text = "n.myagmardorj, z.amarbold , d.batsukh" , font=("Times",11), bg=color, fg=comment_color).place(x=310, y=50)

        Label(self.rootmem, text = "нууц үг нь багадаа 7 тоо, 3 үсэг, 1 том үсэг ", font=("Times",11), bg=color, fg=comment_color).place(x=310, y=220)
        Label(self.rootmem, text = "орсон байх шаардлагатай.    Aab1234567", font=("Times",11), bg=color, fg=comment_color).place(x=310, y=240)
        Label(self.rootmem, text = "түвшингээс хамаарч мэдээллийг зөвхөн харах,", font=("Times",11), bg=color, fg=comment_color).place(x=310, y=150)
        Label(self.rootmem, text = "эсвэл чөлөөтэй өөрчлөх боломжтой", font=("Times",11), bg=color, fg=comment_color).place(x=310, y=170)

        self.combo = Combobox(self.rootmem, values=self.set.level_list, width=19)
        self.combo.current(0)
        self.combo.grid(row=2, column=1, ipady=2)


        Towch3 = Button(self.rootmem, text="  Үүсгэх  ", bg='#E64B1D' , command=self.member_execute, relief='flat' , font=('Consolas',13)).place(x=345,y=350)
        #Towch1.grid(row = 4, column = 0, padx = 50) 
        
        Towch4 = Button(self.rootmem, text="  Цуцлах  ", bg='#E64B1D' , relief='flat' , font=('Consolas',13)).place(x=480,y=350)
        #Towch1.grid(row = 4, column = 0, padx = 50) 

    def member_execute(self):
        Error = 0
        name = self.real_name.get()
        log_name = self.login_name.get()
        new_pass = self.new_pass1.get()
        new_pass_Re = self.new_pass1_Re.get()
        level = self.combo.get()
        
        if (new_pass != new_pass_Re):
            Error += 3

        check = check_password(new_pass)
        check = check.true1()
        
        if(check is 'False'):
            Error += 1

        print(Error)
        if(Error is 3):
            messagebox.showwarning("Анхааруулга", "Нууц үгнүүд зөрж байна")
        elif(Error is 1):
            messagebox.showwarning("Анхааруулга", "Нууц үг шаардлагад хүрэхгүй байна")
        elif(Error is 0):
            print('OK')
        
        print(new_pass, new_pass_Re, name, log_name, level)

user_information = ['n.myagmardorj','admin']
data_sheet = [{'Name': 'admin', 'Pass': '7876asdf222278333723sixy76879w9i373378438838as2365772345434467922040adq16555129923456617234588246532qweiwiwi', 'Level': 'admin'}, {'Name': 'camer', 'Pass': '24822001asis2439wereds2022932394343424490400sisi2299asdf659719384344qiqi', 'Level': 'operator'}, {'Name': 'darga', 'Pass': '5489651020205446qiqiafdd5300129932335456sdfads20530619978494494549431299', 'Level': 'user'}]
a = main_page(se ,user_information,data_sheet)

