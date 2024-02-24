#1
import datetime
current_time = datetime.datetime.now()
print (current_time.day - 5)

#2
import datetime
current_time = datetime.datetime.now()
print ("Yesterday" , current_time.day - 1)
print ("Today" , current_time.day)
print ("Tommorow" , current_time.day + 1)

#3
import datetime
current_time = datetime.datetime.now()
print (current_time.microsecond)

#4
from datetime import datetime
def date_difference_in_seconds(date1, date2):
    datetime1 = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')
    datetime2 = datetime.strptime(date2, '%Y-%m-%d %H:%M:%S')
    difference_seconds = abs((datetime2 - datetime1).total_seconds())
    return difference_seconds
date1 = input("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
date2 = input("Enter the second date (YYYY-MM-DD HH:MM:SS): ")
difference_seconds = date_difference_in_seconds(date1, date2)
print("Difference between the two dates:", difference_seconds)