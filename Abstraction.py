#Abstraction is the act of removing or hiding complex details to focus only on the most important parts 
#of an idea, object, or system.

#A class is abstract only if it contains atleast 1 abstract method and it inherits ABC(abstract base class)
#Abstract method should use @abstractmethod decorator
from abc import ABC,abstractmethod
class BankApp(ABC):

  def database(self):
    print('connected to database')

  @abstractmethod
  def security(self):
    pass

  @abstractmethod
  def display(self):
    pass

#An object cant be created for an abstract class
#We cannot create an object of an abstract class because it is fundamentally incomplete and serves only as a template.
#  Allowing instantiation would create an object with undefined behaviors and unimplemented functionality, which 
# violates core object-oriented programming principles

class MobileApp(BankApp):

  def mobile_login(self):
    print('login into mobile')

  def security(self):
    print('mobile security')

  def display(self):
    print('display')