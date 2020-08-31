f_name = "nikhil"
l_name = "vinay"

print "f_name[0]: " + f_name[0]       # f_name[0]: n
print "f_name[last]: " + f_name[-1]   # f_name[last]: l
print "l_name[0-2]: " + l_name[0:2]   # l_name[0-2]: vi  [0, n)

c = 83
print f_name + str(c)      #nikhil83

print l_name*2        #vinayvinay

print "i" in f_name   #True

if "i" in f_name:
  print "present"

# Note:  
# +    // cancatenate
# *    // repeat
# [:]  // slicing
# []   // indexing

yob = 84

print '%s' " year of birth " '%d' %(f_name, yob) 

f_name = "nikhil"

print f_name[:2]   # [0,2) ni
print f_name[2:]   # khil 

print len(f_name)  # 6

new_fname = f_name.replace("nik", "pik") #pikhil
print new_fname

print f_name.upper()    # NIKHIL

print "NIKHIL".lower()  #nikhil

print f_name.split('k') # ["ni", "hil"]

print f_name.split('k')[1]  # hil

print ":".join("Python")   #P:y:t:h:o:n

##########################################3

print "###################"

course = "Python for Beginners"
print course.find('P')   # prints 0
print course.find('y')   # prints 1
print course.find('z')   # prints -1 means not found
print course.find("Beginners")   # prints 11

print (course.replace("Beginners", "Absolute Beginners"))  #Python for Absolute Beginners
print course      #Python for Beginners, replace is not done inplace

print ("Python" in course)  #prints True

##### string methods

str = "liza"
print (str.capitalize())  #Liza

print(str.replace("za","sa")) #lisa

