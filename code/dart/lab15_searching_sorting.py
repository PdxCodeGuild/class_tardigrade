""" VERSION 1 LINEAR SEARCH """

# def linear_search(nums, value):
#   for i in range(len(nums)):
#       if value == nums[i]:
#           return i

# # index 0  1  2  3  4  5  6  7
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# index = linear_search(nums, 3)
# print(index)

""" VERSION 2 BINARY SEARCH """

def binary_search(nums, low, high, x):
    if high >= low:
        mid = (low + high) // 2
        if nums[mid] == x:
            return mid
        elif nums[mid] > x:
            return binary_search(nums, low, mid - 1, x)
        else:
            return binary_search(nums, mid + 1, high, x)
    else:
        return - 1


nums = [1, 2, 3, 4, 5, 6, 7, 8]
x = 4

result = binary_search(nums, 0, len(nums) - 1, x)

print(f"\nList: {nums}")
if result != -1:
    print(f"\nElement {x} in the list is present at index", str(result) + ".")
    print()
else:
    print("\nElement is not present in the list\n")
