# Dictionary is collection of key-value pair.
# Keys will be a single element
# Values can be a list or list within a list, numbers, etc.

# Dictionary in python is uordered key-val pair collection
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
print (Dict['Tiffany'])
print Dict

# copy
Dict2 = Dict.copy()
print Dict2
Dict3 = Dict
print Dict3

#update
Dict['Tim']=30
print Dict
Dict.update({'Tim':35})
print Dict

#delete key-val pair by key

del Dict['Tim']
print Dict

#items() returns list of tupple pair

print Dict.items()

# insert in dictionary
Dict['Nik'] = 34
print Dict

#insert duplicate, Duplicate is not inserted , it will update the value of key
Dict['Nik'] = 30
print Dict

#Length
print len(Dict)

#print keys
print Dict.keys()

#############################################################################

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
for key in list(Dict.keys()):
    if key in list(Boys.keys()):
        print(True)
    else:       
        print(False)

################################################

#if exact key val pair are same then it will return 0
# first it will cmpare by keys, if keys are same then it will compare by values
# accordingly it will return 1 or -1
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tim':18, 'Charlie':12,'Robert':25}	
print cmp(Girls, Boys)

#### extract key value at specific index

key, val = Boys.items()[0]
print key, val

# extract only key at index
key = list(Boys.keys())[0]
print key
val = list(Boys.values())[0]
print val
