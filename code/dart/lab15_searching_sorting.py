""" VERSION 1 LINEAR SEARCH """

"""
Implement linear search, which simply loops through the given list and check if 
each element is equal to the value we're searching for. If it is, return the index 
at which it was found, otherwise, return a value indicating that it was not found.
"""

# def linear_search(nums, value):
#   for i in range(len(nums)):
#       if value == nums[i]:
#           return i

# # index 0  1  2  3  4  5  6  7
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# index = linear_search(nums, 3)
# print(index)

""" VERSION 2 LINEAR SEARCH AND BINARY SEARCH """

"""
Implement binary search, which requires that a list is sorted and divides its 
search range in half each iteration until it finds its target.
"""

# A - the list
# n - the length of the list
# T - the value we're searching for
# def binary_search(A, n, T):
#     L = 0
#     R = n - 1
#     while L <= R:
#         m = (L + R) // 2
#         if A[m] < T:
#             L = m + 1
#         elif A[m] > T:
#             R = m - 1
#         else:
#             return m
#     return False # unsuccessful


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


#       0  1  2  3  4  5  6  7
nums = [1, 2, 3, 4, 5, 6, 7, 8]
x = 4

result = binary_search(nums, 0, len(nums) - 1, x)

print(f"\nList: {nums}")
if result != -1:
    print(f"\nElement {x} in the list is present at index", str(result) + ".")
    print()
else:
    print("\nElement is not present in the list")
