# Classes Demo

class Point:
    def move(self):
        print("move")
        
    def draw(self):
        print("draw")
        
point1=Point() #creating object
point1.draw() #calling function "draw" defined in class "Point"


point1.x = 10 # creating attribute
point1.y = 20 # creating attribute
print(point1.x)

point2 = Point() #creating object
point2.x = 2 # creating attribute
print(point2.x)

#######################
########################
print()
#########################
#########################
# creating a constructor:



class Point:
    
    def __init__(self, x, y): #this method constructs the parameters x and y
        self.x = x #initialize parameter x
        self.y = y #initialize parameter y
    
    def move(self):
        print("move")
        
    def draw(self):
        print("draw")


point = Point(20, 25) #create a variable to hold specific x and y values

print(point.x)
 

 ###########################################
 ###########################################


class Person:
     def __init__(self, name):
         self.name = name
     def talk(self):
         print(f'Hi, I am {self.name}')
         
         
 
         
john = Person("John Smith") #this initializes the the name of your constructor method/function
john.talk() # this runs the talk method/function  

bob = Person("Bob Smith")
bob.talk()
          
will = Person("bill")
will.talk()
 
 
 
 
 
 
 
 
 
 

