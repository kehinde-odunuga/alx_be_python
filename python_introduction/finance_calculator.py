# Calculate the user’s monthly savings based on inputted monthly income and expenses. 
# It will then project these savings over a year, assuming a fixed interest rate, to demonstrate compound interest’s effect on savings.

monthly_income = int(input("Enter your monthly income: "))
monthly_expense = int(input("Enter your total monthly expenses: "))
monthly_savings = float(monthly_income) - float(monthly_expense)

Projected_savings = monthly_savings * 12 + monthly_savings * 12 * 0.05

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${Projected_savings}.")