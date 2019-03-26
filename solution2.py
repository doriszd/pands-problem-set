# Doris Zdravkovic, March, 2019
# Solution to problem 2

# User is asked to enter a today's day
x = str(input("Please enter today's day:"))
# List of days of the week
l = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# a=days that begin with T
a = "Tuesday" or "Thursday"
# If today's day begins with T print "Yes, today begins with T"
if x == a:
    print("Yes, today begins with 'T'")
# If today's day does not begin with T print "No, today does not begin with T"
else:
    print("No, today does not begin with 'T'")


