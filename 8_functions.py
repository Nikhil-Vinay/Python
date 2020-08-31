### function call, parameter and return value

def func1():
   print "inside func1"
#print "still inside func1"  #indent error
   print "still inside func1"

func1()

# None is an object in python

def square(x):
    print (x*x)

print square(2)  # it will print None

def square(x):   # we can have same name function, for the below codes this suare function will override the
    return x*x   # previous one

print square(2)  # it will print 4

#  Functions in Python are themselves an object, and an object has some value. We will here see how Python treats an object. When you run the command "print square" it returns the value of the object

print square    # function square at 0x7f6423bdf8c0

# argument in function

def multiply(x, y):
    return x*y

print multiply(2,3)  # 6

# default argument

def multiply(x, y=2):
    return x*y

print multiply(4)    # 8
print multiply(5,4)  # 20

#def multiply(x=3, y, z=4):   # not allowed, similar to c++
#    return x*y*z

def printval(x, y):
    print "val of x: ",x
    print "val of y: ",y

printval(y=4, x=3)

# collect all arguments

def func(*args):
    print args

func(1, 2, 3, 4, 5)
