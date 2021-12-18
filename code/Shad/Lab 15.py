def linear_search(nums, value):
    for num in nums:
            if num == value:
                print(nums.index(value))

  
nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = linear_search(nums, 3)
print(index) 


# print(fruits.index('bananas')) # 1