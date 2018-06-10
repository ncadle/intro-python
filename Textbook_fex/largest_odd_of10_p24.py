# Write a program that asks the user to input 10 integers, and then prints the
# largest odd number  that was entered. If no odd number was entered, it 
# should print a message to that effect. 

#How I approached this problem: 
# 1. use a while loop to ask for 10 integers. I would rewrite this with a for loop (introduced in next section).
# 2. compare the entered number to a variable (y). If the integer is odd and 
#    larger than y, bind the value to y.
# 3. if the variable is still 0 afer all integers have been entered, none are odd. 

x = 0
y = 0
count = 0

while count < 10:
    num = int(input('Enter an integer: ')) 
    if num % 2 != 0:
        if y == 0 and abs(num) > y: # if the first integer is negative, compare the absolute value.
            y = num
        elif num > y:
            y = num
    count += 1        
if y == 0:
    print('There are no odd numbers')
else:
    print('The largest odd number is:',y)
    
    