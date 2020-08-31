print("nikhil")
str = "nikhil";
print(str[-1])
def doit():
    print("welcome")
    print("to python")

doit();

my_map = {
    "name":"nikhil",
    "age":32
}

try:
    print(my_map["last_name"])

except KeyError:
    print("Key is not present") 

print(my_map.get("last_name", "Key is not present"))

my_map["last_name"]="vinay"
my_map["last_name"]="vinay2"

print(my_map.get("last_name", "Key is not present"))

name = "nikhil"
age = 34
# method-1 (It works with python 3 and above)
#print(f"Name: {name} and Age: {age}")
# method-2
print "Name: ",name, " Age: ", age
# method-3
print "Name: %s and Age: %d" %(name, age)
print "Name is %s " %name

## Ask Input

newname = raw_input("> your name please ? > ")  # input is available in python 2.6
print "Name is ", newname

# collect aommand line arguments 
#from sys import argv
import sys

#script, file_name = argv
script, file_name = sys.argv
print "script name is %s and file_name is %s" %(script, file_name)

file_obj = open(file_name)  # default open in read mode
print file_obj.read()
file_obj.close();

# remove all data from file
target = open(file_name, 'w+')
target.truncate()
print target.read()

line1 = "hello world!"
line2 = "myself nikhil vinay"
line3 = "i started learning python"
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print target.read()
target.close()
