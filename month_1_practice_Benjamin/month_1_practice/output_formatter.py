# output_formatter.py

def format_output(
    name: str,
    monthly_savings: float,
    annual_savings: float,
    months_needed: float,
    goal: float
):
    # Say hello to the user by name
    print(f"\nHello, {name}!")

    # Tell the user how much they save each month
    print(f"Your monthly savings are: KES {monthly_savings:.2f}")

    # Show what those savings grow to in one year with 5% interest
    print(f"Projected annual savings (with 5% interest): KES {annual_savings:.2f}")

    # Check if the saving goal is achievable
    if months_needed == float('inf'):
        # If savings per month is zero or negative, you can’t reach the goal
        print("With your current expenses, you cannot reach your savings goal.")
    else:
        # Otherwise, tell the user how many months it will take
        print(f"To reach your goal of KES {goal:.2f}, you need {months_needed:.1f} months.")
