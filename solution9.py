#Solution to problem 9
#python second.py moby-dick.txt

#Doris Zdravkovic, March, 2019

#mobi_dick2 file is opened as read mode
with open('mobi_dick2.txt', 'r') as f:
    #File is counted from the first line
    count = 1
    for line in f:
        #For every line in the file another line is added
        count+=1
        #If the number of the line is divided by 2 and there is no remainder, 
        #the line is printed on the screen.
        if count % 2 == 0: 
            print(line)