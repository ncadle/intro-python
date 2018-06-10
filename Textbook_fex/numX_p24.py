# Concatenate X to toPrint numXs times.

# This is used to teach the use of a while loop. 

numX = int(input("Enter how many times you want to print 'X': "))
toPrint = ''

while numX > 0:
    toPrint += 'X'
    numX -= 1
print(toPrint)