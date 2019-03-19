#python squareroot.py

# Doris Zdravkovic, March, 2019.

#The number to calculate the square root of. 
rootof = float(input("Please enter a positive number:"))

#The initial estimate
estimate = 6

# Loop - keep going until the square of estimate is within 0.1 of rootof. 
while abs ((estimate * estimate)- rootof) > 0.1:
    #Newton's method
    #Adapted from: https://web.microsoftstream.com/video/dca7ddaa-9512-4810-a758-237921e6440e
    estimate -=((estimate * estimate )-rootof) / (2 * estimate)
#Print the result
print (f"The square root of {rootof} is approx. {estimate }")