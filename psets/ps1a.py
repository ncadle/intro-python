# This program shows how many months it takes to save for a house deposit 
# based on the assumptions outlined below. 

current_savings = 0
total_months = 0
monthly_interest = 0.04 / 12 # savings compound at 4% p.a., and (4/12)% per month
annual_salary = float(input("What is your annual salary? "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
monthly_salary = annual_salary / 12
portion_down_payment = 0.25 # percent of total_cost required for deposit
deposit = total_cost * portion_down_payment

while current_savings < deposit:
    current_savings += (current_savings * monthly_interest) # add interest from current savings
    current_savings += monthly_salary * portion_saved # add a month of savings  to current savings
    total_months += 1 
print('Number of months',int(total_months))
