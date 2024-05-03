class Phone1:
    def feature1(self):
        print('blutooth')
        
class Phone2:
    def feature2(self):
        print('camera')
        
class phone3:
    def feature3(self):
        print('music')
 
#multiple inheritance       
class SmartPhone(Phone1,Phone2,phone3):
    def feature4(self):
        print('internet')
        
phone=SmartPhone()

print(phone.feature1())
print(phone.feature2())
print(phone.feature3())



class Phone5:
    def feature5(self):
        print('blutooth is ok')
        
class Phone6(Phone5):
    def feature6(self):
        print('camera is ok')
        
class phone7(Phone6):
    def feature7(self):
        print('music is ok')

##multi        
class SmartPhone2(phone7):
    def feature8(self):
        print('internet is ok')
        
        
        
phone2=SmartPhone2()

phone2.feature5()
phone2.feature7()
phone2.feature7()
phone2.feature8()


##Method overriding
        
class phone9:
    def feature7(self):
        print('music is ok')

       
class SmartPhone3(phone9):
    def feature8(self):
        print('internet is ok')
    
    def feature7(self):
        print('gps is not ok')
        
phone4=phone7()
phone4.feature7()        
phone3=SmartPhone3()
phone3.feature7()


##Super() key word

class phone10:
    def feature10(self):
        print('phone is ready')
        
class SmartPhone4(phone10):
    def feature11(self):
        print('smart phone is ready')
        
        super().feature10()
        
phone4 = SmartPhone4()
phone4.feature11()