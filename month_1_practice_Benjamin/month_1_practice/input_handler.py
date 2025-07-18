# input_handler.py

def get_user_input():
    # 1) Ask the user for their name
    name = input("Enter your name: ")

    # 2) Ask for monthly income, convert to float
    monthly_income = float(input("Enter your monthly income (KES): "))

    # 3) Ask for monthly expenses, convert to float
    monthly_expenses = float(input("Enter your monthly expenses (KES): "))

    # 4) Ask for savings goal, convert to float
    savings_goal = float(input("Enter your savings goal (KES): "))

    # 5) Return all values so main can consume them
    return name, monthly_income, monthly_expenses, savings_goal
