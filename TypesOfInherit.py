#Single
    #Parent
       # |
       # |
       # |
       # V 
    #Child


#Multilevel
    #Parent
           # |
           # |
           # |
           # V 
        #Child
            # |
            # |
            # |
            # V 
        #GrandChild

#Multiple 
#Multiple parents single child

#hirarchial
#Multiple childs single parent

#Hybrid
#mix of any 2

#Method resolution order
#Method Resolution Order (MRO) is the exact sequence Python uses to search for a method or attribute in a class hierarchy. 
# It is critically important in multiple inheritance to determine which parent class's method executes when a name collision occurs.
# The Theory Behind MROPython uses a deterministic algorithm called C3 Linearization to calculate the MRO. 

#class A :

#class B(A) :
#class C(A) :
#class D(B,C) :

#first check if the method exists in D . Then check in B,C(left to right). If not present goes deeper to A
#This is called C3 Linearization

#The __mro__ attribute (returns a tuple).
# The .mro() method (returns a list)

#Diamond problem
class A:
    def show(self):
        print("Process inside Class A")

class B(A):
    def show(self):
        print("Process inside Class B")

class C(A):
    def show(self):
        print("Process inside Class C")

class D(B, C):
    pass

# Create an instance of the child class
obj = D()
obj.show()