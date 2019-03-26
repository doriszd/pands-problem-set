# Doris Zdravkovic, March, 2019 
#$ python secondstring.py

# User is asked to input a sentence
sentence = input("Please write a sentence: ")
# Sentence is split into words in a list
words = sentence.split()
# Prints every second word in the sentence and joins the words without commas and parenthesis
print (' ' .join (words[::2]))

