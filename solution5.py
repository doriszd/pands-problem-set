# solution to problem 5. 
# python primes.py

# Input of a positive integer

n = int(input("Please enter a positive integer:"))
# Prime number is always greater than 1
# reference: https://docs.python.org/3/tutorial/controlflow.html
if n > 1:
    for x in range(2, n):
        if (n % x) == 0:
            print("This is not a prime number.")
            break
    else:
        
        print (n, "is a prime number.")
# If the entered number is equal or less than 1 then it is not a prime number   
else:
 
    print(n, 'is a prime number')


