import time
print(time.time())# time in pulses
print("current time::")
print(time.localtime(time.time()))# returns localtime of the system
import calendar	#importing calender class
cal=calendar.month(1999,10)# passing parameter year and month
print(cal)
print(calendar.prcal(2019))# display complete calendar
