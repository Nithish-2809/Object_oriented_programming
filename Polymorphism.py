#Polymorphism means "many forms".

#It allows the same interface (method/operator/function) to behave differently for different objects.

#One interface, multiple implementations.

#1. Method Overriding (Runtime Polymorphism)

#A child class provides its own implementation of a parent class method.

class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

Dog().sound()


#2. Operator Overloading

#Same operator behaves differently for different data types.

print(2 + 3)
print("Hello " + "World")


#3.Built-in Polymorphism

#Same function works with different data types.

print(len("Python"))
print(len([1,2,3]))
print(len({1,2,3,4}))


#Method Overloading in Python?

#Python does NOT support traditional method overloading.

#USE DEFAULT ARGUMENTS INSTEAD

class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

obj = Calculator()

print(obj.add(1, 2))
print(obj.add(1, 2, 3))

#IF LENGTH OF ARGUMENTS IS VARIABLE THEN USE COMMAND LINE ARGUMENTS
