from tkinter import *
Data = [{'Name': 'admin', 'Pass': '7876asdf222278333723sixy76879w9i373378438838as2365772345434467922040adq16555129923456617234588246532qweiwiwi', 'Level': 'admin'}, {'Name': 'camer', 'Pass': '24822001asis2439wereds2022932394343424490400sisi2299asdf659719384344qiqi', 'Level': 'operator'}, {'Name': 'darga', 'Pass': '5489651020205446qiqiafdd5300129932335456sdfads20530619978494494549431299', 'Level': 'user'}]

for i in range(len(Data)):
	sheet_name = Data[i].get('Name')
	if(sheet_name is 'admin'):
		print('bna',i)
		print(Data[i].get('Pass'))

