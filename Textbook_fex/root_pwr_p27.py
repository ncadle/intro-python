# Write a program that asks the user to enter an integer and prints two integers,
# root and pwr, such that 0 < pwr < 6 and root**pwr is equal to the integer
# entered by the user. If no such pair of integers exxists, it should print a 
# message to that effect.


# First, there will always be a combination - integer**1 - but that should be 
# the final combination. 




#find the root and power of an integer.
x = int(input('Enter an integer: '))
root = 1
pwr = 1
while root < abs(x) and root**pwr != abs(x): 
    pwr = 2
    root += 1
    while root**pwr < abs(x) and pwr < 6:
        pwr += 1
if x < 0 and pwr % 2 != 0:
    root = -root
elif root**pwr != abs(x):
    root = x
    pwr = 1
print ('root is:', root, 'pwr is:', pwr)

