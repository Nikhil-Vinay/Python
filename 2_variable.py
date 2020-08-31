# variablr: numbers, list, string, tupple, list, dictionaries

f = 0
print f

f = "nikhil"

print f

#print f + 9          # error
print f + str(9)

del f

# print f  // error not defined as deleted

############# Local and Global variable #######################3

a = 100

#fun()        # eror as called before definition

def fun():
  a = "nikhil"   # local
  print a        # print local a

fun()

print a          # print global a

def fun2():
   global a      # global keyword is mandatory else a will become local variable 
   a = 20
   print a

fun2()
print a
