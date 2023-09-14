num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

print(f"Original numbers: num1 = {num1}, num2 = {num2}")

temp = num1
num1 = num2
num2 = temp

print(f"After swapping: num1 = {num1}, num2 = {num2}")