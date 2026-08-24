#Magic methods (also called dunder methods for "double underscore") are special, built-in methods in Python
#that begin and end with double underscores. 
#They allow you to define how objects behave when used with standard Python operators and built-in functions,
#enabling you to implement operator overloading and tap into Python’s core language features



#self means object itself

class Student :
    name = ""
    age  = 0
    
    def __init__(self,name,age) :
        self.name = name
        self.age = age
        # print("Constructor is called")
        
    def __str__(self) :
        return 'My name is {} and my age is {}'.format(self.name,self.age)
        
    def __add__(self,other) :
        return '{} {}'.format(self.name+other.name,self.age+other.age) 

s1 = Student("Nithish",19)
# print(s1)
s2 = Student("Vikash",20)

# print(s1.age+s2.age)
print(s1+s2)#__add__
print(s1-s2)#__subract__
print(s1*s2)#__mul__
print(s1/s2)#__truediv__


#variables can be declared even out of the class
class Person :
    def __init__(self,name,age):
        self.name = name
        self.age = age
        

p = Person("Nithish","20")
p.gender = "Male"
print(p.gender)


#destructor
#In Python, a destructor is a special method named __del__(). It is automatically called when an object is about 
# to be destroyed or garbage collected. While Python relies on an automatic garbage collector for memory management, 
# the destructor is primarily used to perform non-memory cleanup tasks, such as closing open database connections, 
# releasing network sockets, or closing files

class FileManager:
    def __init__(self, filename):
        print(f"Opening file: {filename}")
        self.file = open(filename, "w")

    # This is the destructor method
    def __del__(self):
        print("Destructor called: Closing the file.")
        self.file.close()

# 1. Object Creation (Triggers __init__)
obj = FileManager("test.txt")

# 2. Object Destruction (Triggers __del__)
del obj
