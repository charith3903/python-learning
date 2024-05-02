#create class 

class phone:
    def say(self, name):
        x=name
        print('hello '+x)
        
        
        
phone1 = phone()
phone1.say("Apple")

phone2 = phone()
phone2.say("nokia")

#self uses

class Fruit:
    def colour(self, colours):
        self.y = colours
        print('this fruit colour is ' + self.y)
        
        
Apple = Fruit()
Apple.colour("red")
print(Apple.y) 
Apple.y = "green"
print(Apple.y) 