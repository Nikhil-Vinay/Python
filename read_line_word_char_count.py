from sys import argv

print "number of arguments:" + str(len(argv))  # number of arguments
if (len(argv) > 1):
    script, filename = argv  # here script as - "filename.py" and filename is first argument
                             # we can also access file name as "filename = argv[-1]
else:
    exit(1)

num_of_char = 0
num_of_word = 0
num_of_line = 0

# readline() method also increases the file pointer to start of next line
#target.readline()
#target.readline()
#target.readline()

import re       # for regex
from os.path import exists  # to check if file exists
# method-2
if exists(filename):
    target = open(filename, 'r')
    for line in target:
        print line
        wordlist = line.split()
        num_of_line += 1
        num_of_word += len(wordlist)
        chars = re.sub(r"[\n\t\s]*","", line)   # replace newline, tab and space with ""
        print chars
        num_of_char += len(chars)
    

    print "char_count = %d, word_count = %d, line_count = %d" %(num_of_char, num_of_word, num_of_line)
    target.close()
else:
    print "File: "+ filename + " doesn't exist"

