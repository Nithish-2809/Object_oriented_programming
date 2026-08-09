class Account :
    def __init__(self,accNo,balance) :
        self.accNo = accNo
        self.balance = balance
        
a = Account(12345,10000)

#Here we have access to change the data from outside the class which is not safe so encapsulation comes into picture
a.balance = 20000
print(a.balance)

class Account :
    def __init__(self,accNo,balance) :
        self.__accNo = accNo
        self.__balance = balance
        
#here __ indicated private variable
# user cannot access it like this(a.__accNo) as its internally named as __className__variable.The user can still access it but actually python is for grown ups

#To access data outside the class or to see the data setter and getter methods are generally used .

class Account :
    def __init__(self,accNo,balance) :
        self.__accNo = accNo
        self.__balance = balance
        
    def get_balance(self) :
        return self.balance
    
    def set_balance(self,balance) :
        #use multiple checks for safetey before setting the variable
        

#wrapping of data,setter and getter methods as a single unit (class) is called encapsulation.
#Encapsulation is used for keeping the data safe and secure
        
