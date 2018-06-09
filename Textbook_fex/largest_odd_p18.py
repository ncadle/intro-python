#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 06:38:38 2018

@author: nick
"""

# Write a program that examines three variables - x, y, and z - and prints the
# largest odd number among them. If none of them are odd, it should print a 
# message to that effect. 

# This problem is similar to the example on page 17, with the test for oddness
# the added.

# Asking for user input is introduced in the next section of the book. Once 
# you know that, you can add the commented code below instead of setting your
# own values for a, b, and c. 

a = 6 # int(input('Enter a number: '))
b = 4 # int(input('Enter another number: '))
c = 3 # int(input('Enter another number: '))

if a >= b and a >= c and a % 2 != 0:
    print('The largest odd number is:',a)
elif b >= c and b % 2 != 0:
    print('The largest odd number is:',b)
elif c % 2 != 0:
    print('The largest odd number is:',c)
else:
    print('None are odd.')
    
