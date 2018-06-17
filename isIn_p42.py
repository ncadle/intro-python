# Write a function that accepts two strings as arguments and returns True if 
# either string occurs anywhere in the other, and False otherwise.

def isIn(str1, str2):
    return str1 in str2 or str2 in str1
