#epoch = a date and time from which a computer measures system time

import time

#print(time.ctime(0)) #convert time expressed in seconds and convert to readable strings, epoch time


#print(time.time()) #return current seconds since epoch


#print(time.ctime(time.time())) #current date and time and convert to readable strings


time_obj = time.localtime() # create a time object based on local time
print(time_obj)

time_obj2 = time.gmtime() #get utc time
print(time_obj2)

#convert time object in readable strings
local_time = time.strftime("%B %d %Y %H:%M:%S", time_obj) #format, time object
print(local_time)