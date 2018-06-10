# This program is the same as 1a, except every six months you get a 7% salary increase.

current_savings = 0
total_months = 0
monthly_interest = 0.04 / 12 # savings compound at 4% p.a., and (4/12)% per month
annual_salary = float(input('What is your annual salary? '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: '))
monthly_salary = annual_salary / 12
portion_down_payment = 0.25
deposit = total_cost * portion_down_payment

while current_savings < deposit:
    current_savings += (current_savings * monthly_interest) # add interest from current savings
    current_savings += monthly_salary * portion_saved # add a month of savings  to current savings
    total_months += 1  
    if total_months % 6 == 0:
        monthly_salary += monthly_salary * semi_annual_raise
    print(total_months,current_savings)
print('Number of months:',int(total_months))
