def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage:
number = int(input("Enter a Number: "))
fact = factorial_iterative(number)
print(f"The factorial of {number} is {fact}")
