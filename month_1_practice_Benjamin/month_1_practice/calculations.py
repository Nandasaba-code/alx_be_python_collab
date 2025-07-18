# This file is responsible for handling user input and calculating monthly savings.
import sys #to be used for exiting the program if expenses exceed income
from input_handler import get_user_input


print("Welcome to the Personal Finance Tracker!")
print("let's calculate your monthly savings.")


# importing names from input_handler.py
name, monthly_income, monthly_expenses = get_user_input()


# calculating monthly savings
calculate_monthly_savings = monthly_income - monthly_expenses

if calculate_monthly_savings < 0:
    print(f"{name}, you are overspending by: {-calculate_monthly_savings:.2f}")
    sys.exit()  # Exit if expenses exceed income 


# calculating annual savings
calculate_annual_savings = calculate_monthly_savings * 12 * 1.05  # projected annual savings with a 5% interest rate.
print(f"Your annual savings are: {calculate_annual_savings:.2f}")


# calculating months to reach a savings goal
calculate_months_to_goal = float(input("Enter your savings goal: "))

if calculate_monthly_savings > 0:
    months_needed = calculate_months_to_goal / calculate_monthly_savings
    print(f"Months needed to reach your savings goal: {months_needed:.1f}")
else:
    print("You cannot reach your savings goal with your current expenses exceeding your income.")