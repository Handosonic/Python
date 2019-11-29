from password_encrypt import encrypt_pass

pas = "12345"
Aa = encrypt_pass(pas)
name = Aa.enco()
print('1-р үеийн Encode', name)

name1 = Aa.encrypt_passv2(name)
print('2-р үеийн Encode', name1)
#
Aa = encrypt_pass(name1)
de_name = Aa.deco()
print('real word:' ,de_name)
de2_name = Aa.deco_v2()
print(de2_name)

