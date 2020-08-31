# What is shallow copy and deep copy ?
#=====================================
# shallow copy
print "shallow copy example: "
l1 = [10, 20, 30]
l2 = l1  # shallow copy
print l1
print l2
l2.append(40)
print l1
print id(l1)
print id(l2)

# need to import copy module for deep copy
import copy
print "\ndeep copy example: "
l1 = [10, 20, 30]
l2 = copy.copy(l1)  # copy.copy and copy.deepcopy are same.
print id(l1)
print id(l2)
print(l1)
print(l2)
l2.append(40)
print(l2)
print(l1)

# What is difference between list and tupple ?
#=============================================

# list is mutable hough tuple is not mutable.

# How multithreading is achieved in Python?
#============================================
# Python has a multithreading package but if you want to multithread to speed your code up
# Python hs a construct called the Global interpreer lock (GIL). The GIL makes sure that only one of your
# threads can execute at any one time. A thread acquires the GIL, does a lottle work, then passes the GIL onto
# the next thread.
# This happens very quickyl so to the human eye it may seem like your threads are executing in parallel, but they# really just taking turns using the same CPU core.
# All this GIL passing adds overhead to execution.

# to achiver real thread we need to import multiprocessing module
# import multiprocessing
#import threading

# How ternary operators are used in python?

x = 20
y = 10
big = x if x > y else y
print big


# What is monkey patching in python?
#===================================

# In python, the term monkey patch only refers to dynamic modification of a class or module at runtime. Consider
# below example.

class Myclass:
   def __init__(self):
       print "Constructor called\n"
   def f(self):
       print "f()"

def monkey_f(self):
    print "monkey_f()"

myclass = Myclass()
myclass.f()

myclass.f = monkey_f
myclass2 = Myclass()
myclass2.f()


# Explain random and shuffle 
#==============================

from random import shuffle

str = ["My", "name", "is", "Nikhil"]
shuffle(str)
print(str)
shuffle(str)
print(str)

# What is python parameter's passing mechanism
#==============================================

# There are two parameters passing mechanism in python.: pass by reference and pass by value
# By default all the parameters are passed by reference to the function. Thus, if you change the value of the
# parameter within the function, the change will reflect in calling function as well.

# the pass by value is that whenever we pass the arguments to function that are type say numbers, string and tupple. This is because of immutable nature of them.

# Explain inheritance in python?
# ================================
