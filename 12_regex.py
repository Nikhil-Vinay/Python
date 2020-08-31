# A regular expression in a programming language is a special text string used for describing a search pattern. It is extremely useful for extracting information from text such as code, files, log, spreadsheets or even documents.

#While using the regular expression the first thing is to recognize is that everything is essentially a character, and we are writing patterns to match a specific sequence of characters also referred as string.

# we needto import module re for using regex

#  Identifiers:
# ==============
#  \d  (any didit/number)
#  \D  (anything except digit)
#  \s  (any space)
#  \S  (anything except space)
#  \w  (any alpha-numeric characters, including _)
#  \W  (anything except alpha_numeric characters including _) 
#  \b  (any charater except newline)

#  Modifiers:
# ===========
#  \d{3,6}  declare digit between 3 and 6, example: 345, 446 ,3466 etc
#  +=       matches one or more
#  ?=       matches 0 or 1
#  *=       matches 0 or more
#  $        match end of a string
#  ^        match start of a string
#  |        match x or y
#  []       range
#  {}       this amount of preceding code

#  White space characters:
# =======================
#  \s       White space
#  \n       New Line
#  \t       tab
#  \r       carriage return

import re
xx = "guru99,education is fun"
r1 = re.findall(r"^\w+",xx)  # from start of string, alphanumeric
r2 = re.findall(r"^\w",xx)   # from start of string, one alphanumeric
r3 = re.findall(r"^\W",xx)   # sfrom tart of string, except alphanumeric
print(r1)
print(r2)
print(r3)

###################################################3

print((re.split(r'\s','we are splitting the words')))   # split the sentence by white space
print((re.split(r's','split the words')))               # split the sentence by character 's'

###################################################

mylist = ["Hi99 Nik", "Hi23 Nikhil", "Hi Vinay"]
for element in mylist:
    z = re.match("(H\w+)\W(N\w+)", element) #element starting with one or more H then, any nonalphanumeic then,
                                            # one or more N 
    if z:
       print (z.groups())  # groups method provides the tupple, z is object, we can't print z directly becuase
                           # match method return an object and it will print address of the object only

print(re.match("(H\w+)\W(N\w+)", "Hi Nikhil")) # print address of the object

#####################################################

patterns = ["software testing", "Nikhil"]
text = "software testing is fun"

for pattern in patterns:
    z = re.search(pattern, text)
    if z:
       print "pattern is found"
    else:
       print "pattern is not found"

######################################################
#find all valid emails

abc = 'guru99@google.com, careerguru99@hotmail.com, users@yahoomail.com, nik-2@gmail.com, nik vingmail.com' 
emails = re.findall(r'[\w\.-]+@[\w\.-]+', abc)
for email in emails:
    print(email)
