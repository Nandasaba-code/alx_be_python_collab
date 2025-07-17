# prompt user for name, monthly income, monthly expenses and savings goal

name = str(input("Enter your name: "))
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
savings_goal = int(input("Enter your savings goal: "))

# Display results

print(f"Hello, {name}!")
print(f"Your monthly income is ${monthly_income}")
print(f"Your total monthly expenses is ${monthly_expenses}")
print(f"Your savings goal is ${savings_goal}")