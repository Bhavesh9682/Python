def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Found the target, return its index
        elif arr[mid] < target:
            left = mid + 1  # Target is in the right half
        else:
            right = mid - 1  # Target is in the left half

    return -1  # Target not found in the list

sorted_list = [1, 3, 5, 7, 9, 12, 15]
target_value = 9

result = binary_search(sorted_list, target_value)

if result != -1:
    print(f"Found {target_value} at index {result}")
else:
    print(f"{target_value} not found in the list")
