# class in python is similar to c++, it is storage af different types of data and methods to access the data.

class myclass():
   def method1(self):
       print "inside class myclass"
   def method2(self, string):
       print "nikhil is learning " + string

obj = myclass()
obj.method1()
obj.method2("class")

# self is similar to this pointer

#############################################################

class myClass():
  def method1(self):
      print("Guru99")
        
  
class childClass(myClass):
  def method1(self):
        myClass.method1(self);  # self should be passed to call base class meythod
        print ("childClass Method1")
        
  def method2(self):
        print("childClass method2")     
         
def main():           
  # exercise the class methods
  c2 = childClass()
  c2.method1()
  c2.method2()

if __name__== "__main__":
  main()

# note: default all methods are virtual and public

################### constructors ##################################

class User:
    name = ""
    __name2 = "vinay"

    def __init__(self, name):
        self.name = name

    def sayHello(self):
        self.__sayHi()
        print("Welcome to python, " + self.name + " " + self.__name2)

    def __sayHi(self):
        print("Hi Nikhil")

User1 = User("nikhil")
User1.sayHello()
print User1.name
#print User1.__name2   # error, accessing to private data
#User1.__sayHi()       # error, calling private method

# note: all data member and functions are default public, to make data or method private, we need to start
#       the name by _
