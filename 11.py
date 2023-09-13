def is_autobiographical(number):
    str_number = str(number)
    counts = [0] * len(str_number)
    for digit in str_number:
        digit = int(digit)
        if digit < len(counts):
            counts[digit] += 1
            print(counts[digit]);
    
    for i, count in enumerate(counts):
        if count != int(str_number[i]):
            return False
    
    return True

# Input
number = int(input("Enter a number: "))

# Check if it's an autobiographical number
if is_autobiographical(number):
    print(f"{number} is an autobiographical number!")
else:
    print(f"{number} is not an autobiographical number.")
