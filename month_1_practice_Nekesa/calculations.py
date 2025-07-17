# prompt user for monthly income and total monthly expenses

monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))
savings_goal = float(input("Enter your savings goal: "))

# calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# calculate projected annual savings with 5% interest
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)
months_to_goal = savings_goal/ monthly_savings

# Display results

print(f"Your monthly savings are ${monthly_savings:.2f}")
print(f"Projected annual savings with 5% interest is ${projected_savings:.2f}")
print(f"Number of months to reach savings goal is {months_to_goal:.2f}")
