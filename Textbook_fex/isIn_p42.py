# Write a function that accepts two strings as arguments and returns True if 
# either string occurs anywhere in the other, and False otherwise.

def isIn(str1, str2):
    """
    Assumes str1 and str2 are strings.
    Returns True if str1 is within str2 and vice versa.
    """
    return str1 in str2 or str2 in str1
