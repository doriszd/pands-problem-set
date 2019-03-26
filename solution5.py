# Doris Zdravkovic, March, 2019 
# Solution to problem 5. 
# python primes.py

# Input of a positive integer
n = int(input("Please enter a positive integer: "))
# Prime number is always greater than 1
# Reference: https://docs.python.org/3/tutorial/controlflow.html
# If entered number is greater than 1, for every number in range of 2 to entered number
# If entered number divided by any number gives remainder of 0, print "This is not a prime number"
if n > 1:
    for x in range(2, n):
        if (n % x) == 0:
            print("This is not a prime number.")
            # Stop the loop 
            break
    # In other cases print "n is a prime number"
    else:
        print (n, "is a prime number.")
# If the entered number is equal or less than 1 then it is not a prime number   
else:
    print(n, 'is a prime number')


