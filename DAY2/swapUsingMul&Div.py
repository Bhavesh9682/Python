# Input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Swapping without using a temporary variable
num1 = num1 * num2
num2 = num1 / num2
num1 = num1 / num2

# Print the swapped values
print("After swapping:")
print("First number:", num1)
print("Second number:", num2)
