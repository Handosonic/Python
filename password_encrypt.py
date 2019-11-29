import random
def rand_decimal():
    return random.randint(10,99)

def rand_hundred():
    return random.randint(0,9)

def rand_thousand():
    int_list = [1,2,3,4,5,6,7]
    return random.choice(int_list)

def rand_num_get_str(a,b,c):
    return str(a)+str(b)+str(c)  

def rand_string():
    str_list = [  'asdd','asis','wiwi','sdfa','adsf','qwer','sisi','qwei','sdfa','zxcv','asdf','ggsa','were','stan','boye','sexy','loli','sixy','aiai','afdd','wweq',
    'asdf','iisi','ghgh','xxzs','2341','1299','29AA','@(#2','sfs3','asdf','299a','wi20','asd3','ads4','ad24','a234','a202','sd22','9w9i','skl[','iire','dd23','adq1',
    '2,,2','sdfa','sdkf','320q','as23','adf1','asdf',',asd','siw2','qiqi','200a','adf3','adfw','##@)','#@#1','AF@@','A((A','FDAS','ss99','asdf','ds20','2002','adf1',
    '3233','asdf','asdf','1234','2234','3423','2341','2929','0400','9494','2394','2304','1101','1345','2020','2001','1997','4065','2394','2344','234#','2345','2343',
    '24-5','2040','3042','3403','2384','2392','2345','3042','2345','3434','3444','4344','4334','3443','9233','3808','8838','3888','8494','9094','4943','3844','3903',
    '1122','2222','2939','3400','3430','8232','8132','8824','5300','5320','5422','5432','6597','6623','6634','6510','3623','3623','3722','3733','3723','3722','3721'
    ]
    return random.choice(str_list)

class check_password(): 
    def __init__(self, chec_word): # string утга авна
        self.chec_word = chec_word
        self.count_limit = 7
        self.vseg_limit = 3
        self.tom_limit = 1
        self.temdeg_limit = 0
        self.count = 0
        self.vseg = 0
        self.tom = 0  # одоогй
        self.temdegtvvd = ['!','@','#','$','%','&','*','~']
        self.temdeg = 0
         
    def true1(self):
        length = len(self.chec_word)
        word = list(self.chec_word)
        for i in range(length):
            if(word[i].isdigit()):
                self.count += 1
            elif(isinstance(word[i],str)):
                self.vseg += 1
            if(word[i].isupper()):
                self.tom = 1
            if any(word[i] in s for s in self.temdegtvvd):
                self.temdeg += 1
        
        if(self.count >= self.count_limit and self.vseg >= self.vseg_limit and self.tom >= 1 and self.temdeg >= self.temdeg_limit):
            #print('shaardlaga hangaj bna')
            #print(self.vseg)
            return 'True'
        else:
            return 'False'

class encrypt_pass(): 
    def __init__(self, name):
        self.name = name # self гэж зарлаж өгвөл бүх функцанд хандаж чадна  
        self.number = 579 # хоёр ижилхэн үсэг байвал дараагийнх дээр нь тоог нэмж өгнө

    def enco(self):
        add = rand_decimal()   # private утгууд 
        add_hundred = rand_hundred()  #
        add_thousand = rand_thousand() #
        b2 = rand_num_get_str(add_thousand,add_hundred,add)
        length = len(self.name)
        word = list(self.name)
        for i in range(length):
            if(word[i] is 'H' or word[i] is 'h'  ):
                word[i] = '1234'
            elif(word[i] is 'e' or word[i] is 'E'):
                word[i] = '1023'
            elif(word[i] is 'l' or word[i] is 'L'):
                word[i] = '1289'
            elif(word[i] is 'o' or word[i] is 'O'):
                word[i] = '1065'
            elif(word[i] is 'a' or word[i] is 'A'):
                word[i] = '1147'
            elif(word[i] is 'u' or word[i] is 'U'):
                word[i] = '1059'
            elif(word[i] is 'b' or word[i] is 'B'):
                word[i] = '1297'
            elif(word[i] is 'c' or word[i] is 'C'):
                word[i] = '1024'
            elif(word[i] is 'd' or word[i] is 'D'):
                word[i] = '1068'
            elif(word[i] is 'F' or word[i] is 'f'):
                word[i] = '1067'
            elif(word[i] is 'J' or word[i] is 'j'):
                word[i] = '1116'
            elif(word[i] is 'G' or word[i] is 'g'):
                word[i] = '1075'
            elif(word[i] is 'I' or word[i] is 'i'):
                word[i] = '1164' 
            elif(word[i] is 'K' or word[i] is 'k'):
                word[i] = '1047' 
            elif(word[i] is 'M' or word[i] is 'm'):
                word[i] = '1217'
            elif(word[i] is 'N' or word[i] is 'n'):
                word[i] = '1193'
            elif(word[i] is 'p' or word[i] is 'P'):
                word[i] = '1035'
            elif(word[i] is 'Q' or word[i] is 'q'):
                word[i] = '1045'
            elif(word[i] is 'R' or word[i] is 'r'):
                word[i] = '1085'
            elif(word[i] is 'S' or word[i] is 's'):
                word[i] = '1268'
            elif(word[i] is 'T' or word[i] is 't'):
                word[i] = '1201'
            elif(word[i] is 'v' or word[i] is 'V'):
                word[i] = '1100'
            elif(word[i] is 'w' or word[i] is 'W'):
                word[i] = '1260'
            elif(word[i] is 'X' or word[i] is 'x'):
                word[i] = '2162'
            elif(word[i] is 'Y' or word[i] is 'y'):
                word[i] = '2338'
            elif(word[i] is 'z' or word[i] is 'Z'):
                word[i] = '2304'
##---------------toonyyd-------------------#
            elif(word[i] is '1'):
                word[i] = '2344'
            elif(word[i] is '2'):
                word[i] = '2301'
            elif(word[i] is '3'):
                word[i] = '2155'
            elif(word[i] is '4'):
                word[i] = '2311'
            elif(word[i] is '5'):
                word[i] = '2161'
            elif(word[i] is '6'):
                word[i] = '2198'
            elif(word[i] is '7'):
                word[i] = '2368'
            elif(word[i] is '8'):
                word[i] = '2290'
            elif(word[i] is '9'):
                word[i] = '2319'
            elif(word[i] is '0'):
                word[i] = '2169'
##------------ Special Тэмдэгт -------------------#
            elif(word[i] is '#'):
                word[i] = '2128'
            elif(word[i] is '!'):
                word[i] = '2264'
            elif(word[i] is '@'):
                word[i] = '2130'
            elif(word[i] is '$'):
                word[i] = '2186'
            elif(word[i] is '%'):
                word[i] = '2039'
            elif(word[i] is '^'):
                word[i] = '2129'
            elif(word[i] is '&'):
                word[i] = '2125'
            elif(word[i] is '*'):
                word[i] = '2054'

        word_2 = ''            
        for i in range(length):
            if(i < length-1):
                if(word[i] is word[i+1]):
                    #print('dawxar vseg bna')
                    word[i+1] = int(word[i+1]) + self.number
            word[i] = int(word[i]) + int(add) - int(add_hundred*100) + int(add_thousand*1000)
            word_2 = word_2 + str(word[i])
        
        return word_2 + b2

    def encrypt_passv2(self, word):
        length = len(word)
        word2 = list(word)  
        #print(length,word2)  
        last = ''
        for i in range(length):
            if(i is 3 or (i+1)%4 is 0 and i > 0):
                last = last + word2[i]
                last = last + rand_string()
                last = last + rand_string()
                #last = last + rand_string()
            else:
                last = last + word2[i]
        return last
        
    def deco(self):
        #print('1-р үеийн decode')
        #print(self.name)
        length = len(self.name)
        #real_lenth = int(length / 12) 
        #print(real_lenth)
        real_counter = 0 ; fake_counter = 0 ; word = '' ; 
        medregch = True
        for i in range(length):
            if(real_counter is 4):
                medregch = False
            if(medregch is False):
                #print('fake nemex:', i)
                fake_counter += 1
                if(fake_counter is 8):
                    medregch = True
                    real_counter = 0
                    fake_counter = 0
            elif(real_counter < 4 and medregch == True):
                word = word + self.name[i]
                #print('word nemex:',i)
                real_counter += 1 
        self.word = word

        # 2-р үеийн Decode-ing
    def deco_v2(self):
        #print(self.word)
        text = self.word
        length = len(text)
        b2 = ''
        b2 = text[length-4] + text[length-3] + text[length-2] + text[length-1]
        length = length - 4
        add = int(b2[2]+b2[3])
        add_hundred = int(b2[1])
        add_thousand = int(b2[0]) ; counter = 0 ; b2 = '' ; word2 = []
        for i in range(length):
            if(counter < 4):
                b2 = b2 + text[i]
                counter+=1 
                if(counter is 4):
                    b2 = int(b2) - add + (add_hundred*100) - (add_thousand*1000)
                    word2.append(b2)
                    #print(b2)
                    counter = 0
                    b2 = ''
        for i in range(len(word2)-1):
            #print(word2[i],word2[i+1]-self.number)
            if(word2[i] == word2[i+1]-self.number):
                word2[i+1] -= self.number 
        for i in range(len(word2)):
            if(word2[i] == 1023):
                word2[i] = 'e'    
            elif(word2[i] == 1234):
                word2[i] = 'h'
            elif(word2[i] == 1289):
                word2[i] = 'l'
            elif(word2[i] == 1065):
                word2[i] = 'o'
            elif(word2[i] == 1147):
                word2[i] = 'a'
            elif(word2[i] == 1059):
                word2[i] = 'u'
            elif(word2[i] == 1297):
                word2[i] = 'b'
            elif(word2[i] == 1024):
                word2[i] = 'c'
            elif(word2[i] == 1068):
                word2[i] = 'd'
            elif(word2[i] == 1067):
                word2[i] = 'f'
            elif(word2[i] == 1116):
                word2[i] = 'j'
            elif(word2[i] == 1075):
                word2[i] = 'g'
            elif(word2[i] == 1164):
                word2[i] = 'i'
            elif(word2[i] == 1047):
                word2[i] = 'k'
            elif(word2[i] == 1217):
                word2[i] = 'm'
            elif(word2[i] == 1193):
                word2[i] = 'n'
            elif(word2[i] == 1035):
                word2[i] = 'p'
            elif(word2[i] == 1045):
                word2[i] = 'q'
            elif(word2[i] == 1085):
                word2[i] = 'r'
            elif(word2[i] == 1268):
                word2[i] = 's'
            elif(word2[i] == 1201):
                word2[i] = 't'
            elif(word2[i] == 1100):
                word2[i] = 'v'
            elif(word2[i] == 1260):
                word2[i] = 'w'
            elif(word2[i] == 2338):
                word2[i] = 'y'
            elif(word2[i] == 2304):
                word2[i] = 'z'
            elif(word2[i] == 2162):
                word2[i] = 'x'
        #----------toonyyyd-------------#
            elif(word2[i] == 2344):
                word2[i] = '1'
            elif(word2[i] == 2301):
                word2[i] = '2'
            elif(word2[i] == 2155):
                word2[i] = '3'
            elif(word2[i] == 2311):
                word2[i] = '4'
            elif(word2[i] == 2161):
                word2[i] = '5'
            elif(word2[i] == 2198):
                word2[i] = '6'
            elif(word2[i] == 2368):
                word2[i] = '7'
            elif(word2[i] == 2290):
                word2[i] = '8'
            elif(word2[i] == 2319):
                word2[i] = '9'
            elif(word2[i] == 2169):
                word2[i] = '0'
        #----- Special Тэмдэгт ---------
            elif(word2[i] == 2128):
                word2[i] = '#'
            elif(word2[i] == 2264):
                word2[i] = '!'
            elif(word2[i] == 2130):
                word2[i] = '@'
            elif(word2[i] == 2186):
                word2[i] = '$'
            elif(word2[i] == 2039):
                word2[i] = '%'
            elif(word2[i] == 2129):
                word2[i] = '^'
            elif(word2[i] == 2125):
                word2[i] = '&'
            elif(word2[i] == 2054):
                word2[i] = '*'        

       # print(word2)
        word3 = ''
        #for i in range(len(word2)):
            #word3 += word2[i]
        #return word3
        return word3.join(word2)