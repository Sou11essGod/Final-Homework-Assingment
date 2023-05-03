#User imports 2 loan outtakes
loan1 = float(input("Enter the amount of your first student loan: "))
interest_rate1 = float(input("Enter the interest rate of your first student loan (as a decimal): "))
loan2 = float(input("Enter the amount of your second student loan: "))
interest_rate2 = float(input("Enter the interest rate of your second student loan (as a decimal): "))

# Calculate total loan amount and monthly payment
total_loan = loan1 + loan2
interest_rate = (interest_rate1 + interest_rate2) / 2
monthly_rate = interest_rate / 12
monthly_payment = (monthly_rate * total_loan) / (1 - (1 + monthly_rate) ** (-120)) 

# Print monthly payment and estimated payoff date
print("Your total loans are: ", total_loan)
print("Your monthly payment will be $%.2f." % monthly_payment)
print("Assuming you make consistent monthly payments, you will pay off your loans in 10 years, which is around", int(120 / 12), "years.")