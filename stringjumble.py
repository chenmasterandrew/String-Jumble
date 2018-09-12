"""
stringjumble.py
Author: Andrew Chen
Credit: https://github.com/HHS-IntroProgramming/String-Jumble
https://stackoverflow.com/questions/9050355/using-quotation-marks-inside-quotation-marks
https://developers.google.com/edu/python/strings

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""
text = input("Please enter a string of text (the bigger the better): ")
print ("You entered \"{0}\". Now jumble it:".format(text))

#Reverses all text
reverseall = ""
for x in range(1,len(text) + 1):
    reverseall += (text[-x])
print (reverseall)

#Reverses word order
reverseword = ""
lastspace = 0
for x in range(1,len(text) + 1):
    if text[x-1] == " ":
        reverseword = text[lastspace:x-1] + " " + reverseword
        lastspace = x
reverseword = text[lastspace: -1] + text[-1] + " " + reverseword
print (reverseword)

#Reverses word order
reverseletter = ""
lastspace = 0
for x in range(1,len(reverseall) + 1):
    if reverseall[x-1] == " ":
        reverseletter = reverseall[lastspace:x-1] + " " + reverseletter
        lastspace = x
reverseletter = reverseall[lastspace: -1] + reverseall[-1] + " " + reverseletter
print (reverseletter)

