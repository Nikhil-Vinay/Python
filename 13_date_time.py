from datetime import date     # if you need only date
from datetime import time     # if you need only time
from datetime import datetime
import datetime

today = date.today()
print today

today = datetime.date.today()  # if only import datetime
print today

print "Date components:", today.day, today.month, today.year
print "Week Day:", today.weekday()  # monday(0), wednesday(1)...

#now =  datetime.now()
