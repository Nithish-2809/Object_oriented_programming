#an object can be created even without storing its reference anywhere.
# In this case the object is created and space is also allocated to it in the memory but the issue is we cannot 
#access this object once the expression is ended. Python garbage collection helps us to reclaim that space to avoid memory wastage.

class Person :
    def __init__(self,name,age):
        self.name = name
        self.age = age
        

Person("Nithish",20)

#p = Person("Nithish",19)
#|
#|--> This is called as reference variable(which contains the address of the object)
# object can have multiple reference variables
#if we change one reference variable then it effects the original object

#You can pass objects as parameters and even return objects in the functions
class Person :
    def __init__(self,name,age) :
        self.name = name
        self.age = age
        

p = Person("Nithish",20)

def greet(p) :
    print("hello {} your age is {}".format(p.name,p.age))
    
greet(p)

#Here actually you are not passing the entire object you are passing the address/reference of the object to the function
