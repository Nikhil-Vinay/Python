# A tuple is just like a list of a sequence of immutable python objects. The difference between list and tuple is that list are declared in square brackets and can be changed while tuple is declared in parentheses and cannot be changed. However, you can take portions of existing tuples to make new tuples #

tup = ()
tup = ("Jan", "Feb", "March")

print tup[0]
# tup[0] = "nik"   # tupple doesn't support item initialization, it has immutable object

tup1 = (2,)  # for single element comma is mandatory in tupple else tup1[0] is not accessible
print tup1[0]

print tup[0:2]   # Jan, Feb

# tupple packing and unpacking

x = ("nikhil", 34, "software engineer")   # packing
(name, age, designation) = x              # unpacking
print name
print age
print designation

#Comparing tuples
#A comparison operator in Python can work with tuples.

#The comparison starts with a first element of each tuple. If they do not compare to =,< or > then it proceed to the second element and so on.

#It starts with comparing the first element from each of the tuples

#Let's study this with an example-

a=(5,6)
b=(1,4)
if (a>b):print("a is bigger")
else: print("b is bigger")

del a

# print a[0]  # error

######### Dictionary itemas are tupples, dixtionary can be a list of tupples #################
a = {'x':100, 'y':200}
print a.items()
b = list(a.items())
print(b)

######### Built in function of tupple #######################

#To perform different task, tuple allows you to use many built-in functions like all(), any(), enumerate(), max(), min(), sorted(), len(), tuple(), etc

tup = (1, 4, 6, 2, 3, 20, 10)
print max(tup)
print min(tup)
print sorted(tup)
print len(tup)
print any(tup)

# Below methods are not applicable for tupple though works for list

#tup.insert(0, 1)
#tup.remove(10)
#tup.append(30)
#tup.pop()

# tup.sort()  # error  , it gives error because tupple ic constant object and we are trying to sort in place
print tup
tup2 = sorted(tup)  # it is ok because we are not changing the tupple, we are assigning sorted tupple to another
print tup2

mytup = (1, "nik")
print mytup
print mytup[0]

mylist = [1, "nik"]

# Note: Look above, in python, list and tupple can have hetrogeneous values
