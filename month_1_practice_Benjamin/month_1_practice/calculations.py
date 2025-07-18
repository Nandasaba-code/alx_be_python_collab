# calculations.py

def calculate_monthly_savings(
    income: float,   # 1st parameter: the money you earn each month (must be a float)
    expenses: float  # 2nd parameter: the money you spend each month (must be a float)
) -> float:          # '-> float' means this function will return a floating‑point number    
    # Subtract your monthly expenses from your income
    # to find out how much you actually save each month.
    return income - expenses

def calculate_annual_savings(
    monthly_savings: float,      # 1st parameter: expected monthly savings as a float
    interest_rate: float = 0.05  # 2nd parameter: expected interest rate as a float, defaults to 0.05 (5%)
) -> float:                      # the '-> float' indicates this function will return a float    
    # Take your monthly savings, multiply by 12 to get yearly savings,
    # then add interest (default 5%) to see how much you’ll have after a year.
    return monthly_savings * 12 * (1 + interest_rate)

def calculate_months_to_goal(
    monthly_savings: float,  # 1st parameter: how much you save each month (float)
    goal: float              # 2nd parameter: your overall savings target (float)
) -> float:                  # '-> float' indicates this function returns a float value    
    # If you’re not saving anything (or spending more than you earn),
    # return infinity to show the goal can’t be reached.
    if monthly_savings <= 0:
        return float('inf')
    # Otherwise, divide your savings goal by how much you save each month
    # to see how many months it will take.
    return goal / monthly_savings
