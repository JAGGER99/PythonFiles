# Inheritance Demo
# this helps duplicate code much faster! Dont define something twice!
class Mammal:
    def walk(self):
        print("walk")
    


class Dog(Mammal): # the class "Dog" inherits all methods in  "Mammal" class
     
        pass # tells Python interpreter keep going and dont worry about there being no code!
        
class Cat(Mammal): # same as line 9

        def bark(self):
            print("bark bark!")  
        
        
dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.bark()