# python list can be homogeneous or hetrogeneous

name = ["nikhil", "vinay"]
print name[0]   # nikhil
print name[-1]  # vinay

name[0] = "putush"

print name[0]  # putush
#print names = []  # creates empty list

name.append("put")

print name[-1]   # put

# Besting a list

latest_name = ["hello", ["nikhil", "vinay"]]

print latest_name[0]

print latest_name[1][1]

####################################################

mylist = [2, 3, "hello", 4 , "nikhil"]

print mylist[2]
print mylist[3]

print mylist

mylist.pop()
print mylist

mylist.remove("hello")
print mylist

mylist.insert(0, "putush")
print mylist

mylist.append("hello")
print mylist

list2 = ["hello", 5]

mylist.append(list2)
print mylist

list = [1, 4, 6, 2, 3, 20, 10]
print max(list)
print min(list)
print sorted(list)
print len(list)
print any(list)

# sort the list
print list
list.sort()
print list

### slicing of list

list = [1, 2, 3, 4, 5]
print list[:]    # print full list
print list[2:3]  # print 3 , equality at first index, non equality at last index
print list[0:-1] # print [1, 2, 3, 4]

# updating the list

list[2] = 10
print list      # [1, 2, 10, 4, 5]

# deleting list elements

del list[0]    # remove element at index 0
print list

# appending in list
list.append("nik")
print list

#length of list
print len(list)

print max(list)  # print nik

length = len(list) 
del list[length-1]  # delete "nik"

print list
print max(list)  # print 10

print min(list)  # print 2

print sum(list)

list.sort()  # sort in ascending order
print list

list.sort(reverse=True)  # sort in descending order
print list

list.reverse()
print list

mylist = [["30", "nikhil"], ["10", "vinay"], ["25", "putush", "5"]]
mylist.sort()  # default key is first element
print mylist
mylist.sort(key=len)  # python len function is used on all elements
print mylist
mylist.sort(key=len, reverse = True)
print mylist

class Student:
   name = ""
   grade = ''
   age = 0

   def __init__(self, name, grade, age):
       self.name = name
       self.grade = grade
       self.age = age

student_objects = [
     Student('john', 'A', 15),
     Student('jane', 'B', 12),
     Student('dave', 'B', 10),
   ]

student_objects.sort(key=lambda student: student.age)   # sort by age

mylist = [[10, "nikhil"], [20, "Anand"]]
mylist.sort(key=lambda x:(x[1]))  # we can sort by multiple attribute as key=lambda x:(x[1], x[3])
print mylist

mylist2 = mylist
print mylist2

tupple = (1, 2, 3) # tupple
print tupple
#mylist = list(tupple)
#print mylist
print "#########################"

nums = [1, 2, 3]
print (10 in nums)
x, y, z = nums
print "x: %d, y: %d, z: %d" %(x,y,z)

nums.append(4)
print nums

#===============================================
print ("edx learning")
det = [["nik", 10]]
print (det)
print (type(det))      # list
det = det + ["vin", 20]
print (det)

del(det[0])
print(det)

x = ["a", "b"]
print(x.index("b")) # 1

# Question: How can list store different types of data together?
# Ans: List actually contains array of references, It doesn't contain array of data insteat it contains reference
#      of the data (data stored at different localtions). This is how it manages to store different types of data#.     When we update an list at any index, it deletes the old reference and creates memory for new data and stor#      e new reference in the list. SO, integer can be replaced with  character(or any data type) in python list

# list methods:
#list.sort(key=None, reverse=False)
#Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

#list.reverse()
#Reverse the elements of the list in place.

#list.copy()
#Return a shallow copy of the list. Equivalent to a[:].

#list.clear()
#Remove all items from the list. Equivalent to del a[:].

#list.index(x[, start[, end]])
#Return zero-based index in the list of the first item whose value is x. Raises a ValueError if there is no such item.

#list.append(x)
#Add an item to the end of the list. Equivalent to a[len(a):] = [x].

#list.extend(iterable)
#Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

#list.insert(i, x)
#Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

#list.remove(x)
#Remove the first item from the list whose value is x. It is an error if there is no such item.

#The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

#list.count(x)
#Return the number of times x appears in the list.

#list.pop([i])
#Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

# Qn: How to use list as stack?

# >>> stack = [3, 4, 5]
#>>> stack.append(6)
#>>> stack.append(7)
#>>> stack
#[3, 4, 5, 6, 7]
#>>> stack.pop()
#7
#>>> stack
#[3, 4, 5, 6]
#>>> stack.pop()
#6
#>>> stack.pop()
#5
#>>> stack
#[3, 4]

#QN: How to use list as que?

# It is also possible to use a list as a queue, where the first element added is the first element retrieved (“first-in, first-out”); however, lists are not efficient for this purpose. While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).

#To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends. For example:

#>>>
#>>> from collections import deque
#>>> queue = deque(["Eric", "John", "Michael"])
#>>> queue.append("Terry")           # Terry arrives
#>>> queue.append("Graham")          # Graham arrives
#>>> queue.popleft()                 # The first to arrive now leaves
#'Eric'
#>>> queue.popleft()                 # The second to arrive now leaves
#'John'
#>>> queue                           # Remaining queue in order of arrival
#deque(['Michael', 'Terry', 'Graham'])
