print("Nikhil", "vinay")
# seperator print supported in above version
#print("Nikhil", "vinay", sep="\n")    # Nikhil and vinay are in different line
#print("Nikhil", "vinay", sep='@')     #Nikhil@Vinay  

# iteration, iterable, iterator
l1 = [1, 2, 3]  # l is iterable
for i in l1:    # i is iterator, this process is called iteration
   print(i)

# right hand side is always object on heap [1, 2, 3] is stored in heap
# left hand side is stored on stack, l is stored at stack
# list is mutable

print (id (l1))
l2 = l1
print (id(l2))
l2[0] = 4
print l1    # 4, 2, 3

# strings are immutable

str1 = "nikhil"
# str1[0] = 'p'   # no allowed
print(id(str1))

str1 = str1.replace('n', 'p')  # it will work but new object will be assigned to str1, old obj is deleted
                               # garbage collector, so now id of str1 is changed
print(id(str1))
print(str1)
