import random 
  
# using choice() to generate a random number from a  
# given list of numbers. 
print ("A random number from list is : ") 
print (random.choice([1, 4, 8, 10, 3])) 
  
# using randrange() to generate in range from 20 
# to 50. The last parameter 3 is step size to skip 
# three numbers when selecting. 
print ("A random number from range is : ") 
print (random.randrange(20, 50, 3)) 

# using random() to generate a random number 
# between 0 and 1 
print ("A random number between 0 and 1 is : ") 
print (random.random()) 
  
# using seed() to seed a random number 
random.seed(5) 
  
# printing mapped random number 
print ("The mapped random number with 5 is : ") 
print (random.random()) 
