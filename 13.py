def second_largest(arr):
    if len(arr) < 2:
        return "Array should contain at least two elements"
    
    first_max = max(arr[0], arr[1])
    second_max = min(arr[0], arr[1])
    
    for num in arr[2:]:
        if num > first_max:
            second_max = first_max
            first_max = num
        elif num > second_max and num != first_max:
            second_max = num
    
    return second_max

# Example usage
input_array = [12, 5, 9, 20, 15]
result = second_largest(input_array)
print(f"The second largest number is: {result}")
