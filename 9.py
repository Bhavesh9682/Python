# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return -1  # Target not found

# # Example usage
# sorted_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# target = 12
# result = binary_search(sorted_list, target)

# if result != -1:
#     print(f"Target {target} found at index {result}")
# else:
#     print(f"Target {target} not found")



def linear_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1  # Target not found

# Example usage
my_list = [4, 2, 8, 1, 6, 3, 7, 5]
target = 6
result = linear_search(my_list, target)

if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print(f"Target {target} not found")
