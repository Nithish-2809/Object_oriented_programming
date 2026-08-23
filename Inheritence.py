#INHERITENCE
#Inheritance allows a new class (child or subclass) to adopt the attributes and methods of an existing class (parent or superclass).
#Inheritence represents is-a relationship

# Parent Class
class Animal:
    def eat(self):
        print("This animal eats food.")

# Child Class
class Dog(Animal):
    def bark(self):
        print("The dog barks.")

# Testing the code
my_dog = Dog()

# The dog uses the eat function from Animal
my_dog.eat()   # Output: This animal eats food.

# The dog uses its own function
my_dog.bark()  # Output: The dog barks.

#What gets inherited????????????????
#constructor
#non private members
#non private methods

#inside child class if there is no constructor then automatically the parent constructor is called.But if there is
#a child constructor then we have to call the parent constructore manually not like default in java.



#Aggregation
#Aggregation is when one class borrows or holds another independent class as a part of itself.
#Aggregation represents has-a relationship


class Address :
    def __init__(self,street,pin,city) :
        self.street = street
        self.pin = pin
        self.city = city

class Customer :
    def __init__(self,name,age,address) :
        self.name = name
        self.age = age
        self.address = address
    
    def print_address(self) :
        print(self.address.street,self.address.pin,self.address.city)

add1 = Address("BHEL TOWNSIP",502032,"Hyderabad")
cust1 = Customer("Nithish",20,add1)

cust1.print_address()

#Private variables cant be accessed in aggregation we should use getter and setter methods


