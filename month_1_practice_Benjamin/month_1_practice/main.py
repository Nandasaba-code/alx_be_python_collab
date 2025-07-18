# main.py
import sys

from input_handler import get_user_input
import calculations
from output_formatter import format_output

def main():
    # 1) Greet the user and explain what the program does
    print("Welcome to the Personal Finance Tracker!")
    print("Let's calculate your monthly savings.\n")

    # 2) Ask the user for their name, income, expenses, and savings goal
    name, monthly_income, monthly_expenses, savings_goal = get_user_input()

    # 3) Figure out how much they save each month
    monthly_savings = calculations.calculate_monthly_savings(
        monthly_income,
        monthly_expenses
    )

    # 4) If they spend more than they earn, warn them and stop
    if monthly_savings < 0:
        overspend = -monthly_savings
        print(f"{name}, you are overspending by: KES {overspend:.2f}")
        sys.exit()

    # 5) Otherwise, project what those savings become in a year (with interest)
    annual_savings = calculations.calculate_annual_savings(monthly_savings)

    # 6) Calculate how many months it will take to hit their savings goal
    months_needed = calculations.calculate_months_to_goal(
        monthly_savings,
        savings_goal
    )

    # 7) Send all the results to the formatter to print neatly
    format_output(
        name,
        monthly_savings,
        annual_savings,
        months_needed,
        savings_goal
    )

# Only run main() if this script is executed directly (not imported)
if __name__ == "__main__":
    main()
