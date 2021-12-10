#Big_O Notation



"""
def linear_search(nums, value):
    for i in range(len(nums)):
        if nums[i] == value:
            return i
    return False
            

nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = linear_search(nums, 4)
print(index) 

"""
#Linear Search Complete

#Beginning Binary Search


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def binary_search(nums, value):
    L = 0
    H = len(nums) - 1
    while L <= H:
            mid = (L + H) // 2    
    
            if value < nums[mid]:
                H = mid - 1
            elif value > nums[mid]:
                L = mid + 1
            else:
                return mid
    return None

index = binary_search(nums, 20)
print(index)



#END of Binary Search

#Beginning of Bubble Sort
