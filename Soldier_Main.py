from graphic import login_pass
from graphic import duud
from login_data import get_login_information
from settings import Settings
from main_page import main_page

se = Settings()

a = get_login_information()
data_sheet = a.data_return()
user_information = ['','','']
print(data_sheet)

#data_sheet = [{'Name': 'admin', 'Pass': '7876asdf222278333723sixy76879w9i373378438838as2365772345434467922040adq16555129923456617234588246532qweiwiwi', 'Level': 'admin'}, {'Name': 'camer', 'Pass': '24822001asis2439wereds2022932394343424490400sisi2299asdf659719384344qiqi', 'Level': 'operator'}, {'Name': 'darga', 'Pass': '5489651020205446qiqiafdd5300129932335456sdfads20530619978494494549431299', 'Level': 'user'}]

a = login_pass(data_sheet, user_information)
print(a)
b = a.login()
print(b)

#логин хуудсыг x лэхэд дараагийн хуудас гарч ирж байгаа алдааг засах
#print('looop stoped')

#user_information = ['darga','user']
if(user_information[2] is 1):
	#if check_main(user_information[0]):
	a = main_page(se,user_information, data_sheet)




