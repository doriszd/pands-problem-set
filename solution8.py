# Doris Zdravkovic, March, 2019
#$ python datetime.py

# Import datetime
from datetime import datetime
# Current date and time
now = datetime.now()
# Curent day of the week
day = now.strftime("%A")
print(day, end=", ");
# Current month
month = now.strftime("%B")
print(month, end= " ");
# Current date
day = now.strftime("%d")
# For dates 1, 21, 31 - print ending st
for i in day:
    if i == 1 or i == 21 or i == 31:
        print (day + 'st', end= " ");
        # For dates 2 and 22 - print ending nd
    if i == 2 or i == 22:
        print (day + 'nd', end= " ");
        # For dates 3 and 23 - print ending rd
    if i == 3 or i == 23:
        print (day + 'rd', end= " ");
# In other cases print ending th
else:
    print (day + 'th', end= " ");
# Current year
year = now.strftime("%Y")
# Print year
print(year + '', end= " ");
# Print time in format (hours, minutes), excluding 0
time = now.strftime("%I:%M%p").lstrip('0').replace(' 0', '')
print("at", time, end= " ");





