#static typing
#Static typing is a programming approach where variable data types are checked and known at compile time,
# before the program runs.eg : C,C++,JAVA use static typing. This improves type safetey

int a = 5;
#declaring the type of a at compile time

#dynamic typing
#Dynamic typing is a programming feature where a variable's data type is checked and assigned at run time,
#  rather than fixed when writing code.e.g python,js use dynamic typing 

a = 5

#the type of a is checked and assigned at run time


#static binding

#Static binding means that a function or method call is resolved at compile time rather than at runtime.Also 
# called early binding


#include <iostream>

// Function 1: Expects an integer
void print(int x) {
    std::cout << "Printing an integer: " << x << "\n";
}

// Function 2: Expects a double (decimal number)
void print(double x) {
    std::cout << "Printing a double: " << x << "\n";
}

int main() {
    // The compiler locks in Function 1 at compile time
    print(5);    // Outputs: Printing an integer: 5

    // The compiler locks in Function 2 at compile time
    print(5.5);  // Outputs: Printing a double: 5.5
    
    return 0;
}




#dynamic binding
#Dynamic binding means that a function or method call is resolved at runtime rather than at compile time.Also 
# called late binding


class Dog:
    def speak(self): return "Bark!"

class Cat:
    def speak(self): return "Meow!"

# Dynamic binding happens here:

def animal_sound(animal_obj):
    print(animal_obj.speak()) # Python decides which speak() to run at runtime

