# What is Polymorphism?
# Polymorphism is taken from the Greek words Poly (many) and morphism (forms). 
# It means that the same function name can be used for different types. This makes programming more intuitive and easier.


# Polymorphism in Python
# A child class inherits all the methods from the parent class. 
# However, in some situations, the method inherited from the parent class doesn’t quite fit into the child class. 
# In such cases, you will have to re-implement method in the child class.


class Tomato(): 
     def type(self): 
       print("Vegetable") 
     def color(self):
       print("Red") 
class Apple(): 
     def type(self): 
       print("Fruit") 
     def color(self): 
       print("Red") 
      
def func(obj): 
       obj.type() 
       obj.color()
        
obj_tomato = Tomato() 
obj_apple = Apple() 
func(obj_tomato) 
func(obj_apple)


# Polymorphism with Class Methods


class Bangladesh():
     def capital(self):
       print("Dhaka")
 
     def language(self):
       print("Bangla and English")
 
class USA():
     def capital(self):
       print("Washington, D.C.")
 
     def language(self):
       print("English")
 
obj_ban = Bangladesh()
obj_usa = USA()
for country in (obj_ban, obj_usa):
    country.capital()
    country.language()