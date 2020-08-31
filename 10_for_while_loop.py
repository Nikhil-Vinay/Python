## for, while loop, continue, break

def main():
    x = 2
    while(x != 0):
       print x
       x -= 1        # --x or x-- are not supported

    print "##############"
    for x in range(2,5):     # [2,5)
       print x
 
    for x in range(2,6,2):   # [2,6) with interval 2
       print x

    print "################"
    for x in (5, 10, 20):
       print x

    print "################"
    Months = ["Jan", "Feb", "March", "April", "May", "june", "July", "August", "Sep", "Oct", "Nov", "Dec"] #list
    for x in Months:
       print x
    print "################"
    Days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday") #Tupple
    for x in Days:
       print x
    print "################"
    Dict = { 1:'a', 2:'b' }
    for x in list (Dict.keys()):
      print x
    for x in list(Dict.values()):
      print x

if __name__ == "__main__":
     main()

############## continue and break statement
print "###########################"

def main():
    x = 10
    while( x > 0):
       print x
       x = x-1
       if(x > 5): continue
       else: break

if __name__ == "__main__":
   main()
