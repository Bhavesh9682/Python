def calculate_compound_interest(principal, rate, time, compounding_frequency):
    # Convert the annual interest rate to decimal form
    rate_decimal = rate / 100

    # Calculate the amount
    amount = principal * (1 + (rate_decimal / compounding_frequency))**(compounding_frequency * time)

    # Calculate the interest earned
    interest = amount - principal

    return amount, interest

# Input values
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (as a percentage): "))
time = float(input("Enter the number of years: "))
compounding_frequency = int(input("Enter the number of times interest is compounded per year: "))

# Calculate compound interest
final_amount, earned_interest = calculate_compound_interest(principal, rate, time, compounding_frequency)

# Print the results
print(f"Final amount after {time} years: ${final_amount:.2f}")
print(f"Interest earned: ${earned_interest:.2f}")
