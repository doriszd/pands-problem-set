# python datetime.py
# solution to problem 8

# function datetime is imported from python as dt
import datetime as dt
# function now - the exact time when the function was run.
dt.datetime.now()
# the format is: day of the week, month, date, year, hour, minutes
dt.datetime.strftime(dt.datetime.now(), "%A, %B, %d, %Y, %I, %M%p")

print (dt.datetime.strftime(dt.datetime.now(), "%A, %B %dth %Y at %I:%M%p")) 


