# main method is only needed in method is we want execute the script starting from main method. Once a python script has a main method, it will start executing from there only.

def main():
  print "Hello World!"
  
def doit():
  print "nikhil"

if __name__== "__main__":  # mandatory to call main function
  main()

print "Guru99"

doit()
