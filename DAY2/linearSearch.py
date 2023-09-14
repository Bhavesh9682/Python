def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target if found
    return -1  # Return -1 if the target is not found in the list

my_list = [1, 5, 7, 9, 12, 15]
target_value = 9

result = linear_search(my_list, target_value)

if result != -1:
    print(f"Found {target_value} at index {result}")
else:
    print(f"{target_value} not found in the list")
