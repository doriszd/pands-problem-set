# Doris Zdravkovic, February, 2019
# Solution to problem 1

# User is asked to enter a positive integer
x = int(input("Please enter a positive integer: "))
# a = range of all numbers from 1 to entered number
a = range(1, x)
# b = sum of all numbers in a range from 1 up to entered number
b = sum(a)
# Print the sum of all numbers up to entered number
print (b)
# If entered number is lower than 0 print "Please enter integer greater than 0"
if x < 0:
    print ("Please enter integer greater than 0")