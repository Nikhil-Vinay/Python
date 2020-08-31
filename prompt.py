def prompt():
  print("Please enter an integer value: ")

# Start of program
print("This program adds together two integers.")
prompt() # Call the function
value1 = int(input("Testing to get input from console"))   # all console input are string so, convert it into integer
prompt() # Call the function again
value2 = int(input())
sum = value1 + value2;
print (value1, "+", value2, "=", sum)
