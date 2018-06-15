# What is the decimal equivalent of the binary number 10011?
# This program finds the decimal equivalent of any binary number 

binary = '10011'
x = 0
decimal = 0

for i in binary[::-1]:
    if i == '1':
        decimal += 2**x   
    x += 1
    print(i,x)
print(decimal)        
        
