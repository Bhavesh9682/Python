def is_palindrome(number):
    # Convert the number to a string
    num_str = str(number)
    
    # Compare the string with its reverse
    if num_str == num_str[::-1]:
        print("Number is palindrome")
    else:
        print("Number is not palindrome")

# Test cases
n = input("enter a number")
is_palindrome(n)

