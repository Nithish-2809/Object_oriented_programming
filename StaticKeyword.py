#instance variables are that which are different for different objects of the class(dependent on the object).

#static keyword defines the member belongs to the class itself

#Static variables are independent of the objects whereas the instance variables are dependent on the objects.

class Car :
    speed = 0
    color = ""
    
    def __init__(self,speed,color) :
        self.speed = speed
        self.color = color
        
    @staticmethod
    def isOverspeedVehicle(speed) :
        return speed>=350

c1 = Car(380,"Black")
c2 = Car(200,"Grey")

print(Car.isOverspeedVehicle(c1.speed))
print(Car.isOverspeedVehicle(c2.speed))


#Decorator is used here because generally every object calls the first parameter as the object itself to any instance 
#method and if we dont specify static method using the decorator the method recieves 2 parameters as python internally
#treats it as the instace method so this cause an error.To avoid this we specify the method as @staticmethod


#static variables use=ually start with classname
#eg ATM.numberOfUsers

class Student:
    college = "ABC College"   # static/class variable

    def __init__(self, name):
        self.name = name       # instance variable


s1 = Student("Nithish")
s2 = Student("Rahul")

print(s1.college)
print(s2.college)
print(Student.college)#as every student belongs to same college genrally accessing like this is preffered.

#static methods and static variables can we used even without creation of the objects