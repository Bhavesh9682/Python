def calculate_simple_interest(principal, rate, time):
    # Convert the annual interest rate to decimal form
    rate_decimal = rate / 100

    # Calculate the interest
    interest = principal * rate_decimal * time

    return interest

# Input values
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (as a percentage): "))
time = float(input("Enter the number of years: "))

# Calculate simple interest
interest_amount = calculate_simple_interest(principal, rate, time)

# Print the result
print(f"Simple interest amount: {interest_amount:.2f}")





def calculateSimpleInterest(principal, rate, time):
    rate_decimal = rate/100
    interest = principal * rate_decimal * time
    return interest

principal = float(input("Enter the principal amount"));
rate = float(input("Enter the rate of interest"));
time = float(input("Enter the number of years"));
simple_interest = calculateSimpleInterest(principal, rate, time)
print(f"simple interest: {simple_interest}")


