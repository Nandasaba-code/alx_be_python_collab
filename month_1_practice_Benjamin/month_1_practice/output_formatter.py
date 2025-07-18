# output_formatter.py

from calculations import calculate_monthly_savings, calculate_annual_savings, calculate_months_to_goal


def format_output(name, monthly_income, monthly_expenses):
    monthly_savings = calculate_monthly_savings(monthly_income, monthly_expenses)
    print(f"\nHello, {name}")  # fixed newline
    print(f"Your monthly savings are: KES {monthly_savings:.2f}")

    annual_savings = calculate_annual_savings(monthly_savings)
    print(f"Projected annual savings (with 5% interest): KES {annual_savings:.2f}")

    months_needed = calculate_months_to_goal(monthly_savings)
    if months_needed == float('inf'):
        print("With your current expenses, you cannot reach your savings goal.")
    else:
        print(f"Months needed to reach your savings goal: {months_needed:.1f}")
