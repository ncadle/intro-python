# This program calculates the optimal savings rate based on user inputs of an 
# annual salary to save the required despoit for a $1 million house within
# 36 months (to the nearest $100). The key learning objective here is how to
# use a bisection search algorithm. 

steps = 0
total_months = 36
monthly_interest = 0.04 / 12
total_cost = 1000000
deposit = total_cost * 0.25
current_savings = 0
annual_salary = float(input('What is your annual salary? '))
semi_annual_raise = 0.07
high = 10000
low = 0

while abs(current_savings - deposit) > 100: # use the outer loop to run the bisection search algorithm
    current_savings = 0
    monthly_salary = annual_salary / 12 # reset the value of monthly_salary each time through the loop.
    portion_saved = (high + low) // 2
    total_months = 36 # reset the value of total_months each time through the loop.
    while total_months > 0: # use the inner loop to calculate the depsot saved 
        current_savings += current_savings * monthly_interest 
        current_savings += monthly_salary * (portion_saved / 10000)
        total_months -= 1
        if total_months % 6 == 0:
            monthly_salary += monthly_salary * semi_annual_raise    
    if current_savings < deposit: # if the estimate is to high or low, change the search parameter
        low = portion_saved
    else:
        high = portion_saved    
    steps += 1 
    if portion_saved >= 9999: # this is the way I decided to determine if a salary could ever achieve the required saving
        break
if portion_saved >= 9999:
    print('It is not possible to pay down the loan in three years')
else:        
    print('Best savings rate:',portion_saved/10000)
    print('Number of steps in bisection search:',steps)

# the cut off point is 66163 is too low, 66164 will get you there
    
    