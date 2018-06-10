# Let s be a string that contains a sequence of decimal numbers separated
# by commas, e.g. s = '1.23,2.4,3.123'. Write a program that prints the 
# sum of the numbers in s.

# How I thought about this problem: iterate through the string using a for
#loop by adding each character to a string. When you get to a comma, 
#or the end of the string, convert the string to a float and sum it.

# there is something unsatisfying about this solution because of the repeated
# total += float(sum_string) line, which is needed to get the final number. 

s = '1.23,2.4,3.123'
sum_string = ''
total = 0

for i in  s:
    if i != ',':
        sum_string += i
    else:
        total += float(sum_string)
        sum_string = ''
total += float(sum_string) 
print(total)