#!/usr/bin/python

import os, sys

def check_size(path, limit):
    sz = 0
    f = open('Report.txt', 'w')
    
    for dirName, subdirlist, filelist in os.walk(path):
        for file in filelist:
            try:
                sz = os.path.getsize(dirName + '/' + file)
            except Exception as e:
                f.write(str(e))
            if (sz / 1024 / 1024) > limit:
                f.write( "\n Path: " + dirName + '/' + file + " Size (MB): " + str(sz / 1024 / 1024))
    f.close()

    print '\n Generated Report.txt'

try:
    
    path = sys.argv[1]
    limit = int(sys.argv[2])

except Exception as e:
    print "Usage " + sys.argv[0] + " <path> <limit in MB>"
    sys.exit(0)

check_size(path, limit)


