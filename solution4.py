#Solution4.py
#python collatz.py

#Defining the function here. The function takes a number.  
def collatz(number):
#If the number in collatz function is even, it is divided by 2. 
    if number % 2 == 0:
        #Numbers are printed on a horizontal line. 
        print(number // 2, end=" ")
        #Return the value.
        return number // 2
#If it is an odd number. It is divided by 2 with remainder of 1. The number is multiplied by 3 and 1 is added. 
    elif number % 2 == 1:
        result = 3 * number + 1
        #Numbers are printed on a horizontal line. 
        print(result, end=" ")
        #Return the value.
        return result
#User is asked to enter a number. 
n = input("Please enter a number: ")
#While the value of number does not equal 1, assign the output of the function as a new value and run the function again. 
while n != 1:
    n = collatz(int(n))