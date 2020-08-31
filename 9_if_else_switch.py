## If, Else, Switch

def main():
    x = 2
    y = 3
    if(x < y):
      st = "x is less than y"  # x = 5, in this case st is not initialized so, it print sr will show error
    print st

if __name__ == "__main__":
    main()

##################################################################

def main():
    x = 5
    y = 3
    if(x < y):
      st = "x is less than y"
    else:
      st = "x is greater than/equal y"
    print st

if __name__ == "__main__":
   main()
 
##################################################################33
def main():
    x, y = 2, 2   # interesting
    if(x < y):
      st = "x is less than y"
    elif(x > y):
      st = "x is greater than y"
    else:
      st = "x is equal to y"
    print st

if __name__ == "__main__":
   main()

#####################################################################

def main():
  x, y = 2, 4
  st = "x is greater tha y" if (x > y) else "x is less than equal y"
  print st

if __name__ == "__main__":
   main()

### Nested if can be handled similarly

# python doesn't have switch statement
# python uses dictionary mapping to implement switch statement

def switchExample(argument): 
    switcher = {
        0: "This is Case Zero",
        1: " This is Case One",
        2: " This is Case Two",
    }
    return switcher.get(argument, "nothing")   # nothing is used for default, if switcher won't get anything as
                                               # argument, switcher is a dictionary herei

print switchExample(2)
