# creating a file , opening a file
f= open("nik.txt","w+")  # w - write, r - read, a - append

# write in a file
for i in range(10):
     f.write("This is line %d\r\n" % (i+1))

# close a file
f.close()

#read the file
f = open("nik.txt", "r")
if f.mode=="r":
  contents = f.read()
  print contents

# read the file line by line
f = open("nik.txt", "r")
lines = f.readlines()
print "printing the file line by line:"
for line in lines:
    print line

#remove all contents
f = open("nik.txt", "w+")
f.truncate()
print "printing after truncate"
print f.read()
