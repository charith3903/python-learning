##method overriding
class Parent:
    def func(self):
        print('hellow')
    
class Child(Parent):
    def func(self):
        print('hi')

myobj = Child()
print(myobj.func()) 

#metho overloading

 

class cale:
    sum=0
    def add(self,a=None,b=None,c=None):
        if a != None and b!= None and c!= None:
            sum = a+b+c
            print(sum)
        elif a != None and b!= None:
            sum = a+b
            print(sum)
        else:
            sum = a
            print(sum)
       
       
myo1 = cale()
myo1.add(2,3)
myo1.add(2,3,88)
myo1.add(2)