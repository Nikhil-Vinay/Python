# arithmetic operator ->  + - * / %

x = 10
y = 3
print x+y  # 13
print x-y  # 7
print x*y  # 30
print x/y  # 3
print x%y  # 1
print x**y  # 1000  ** is exponent operator

# comparison operator ==, != , <>, >,<=, etc

# shift operator >> <<

x = 1
print x      # 1
print x<<1   # 2

# assignment operator +=, - = , *=, /= , etc

# Logical operator and, or and not
# returns True, False

x = 1
y = 1

if x and y :
   print "equal"

# ibtwise operator & | ^

print x^y
print x & y

# membership operator
list = [1, 2, 3, 4, 5 ]

if 4 in list:
  print "4 presenet in list"

if 10 not in list:
  print "10 not present in list"

# is, is not operator
x = 10
y = 20

if x is y:
  print "x and y are equal"

if x is not y:
  print " x and y are not equal"
