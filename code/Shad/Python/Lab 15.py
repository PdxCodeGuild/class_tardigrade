def linear_search(nums, value):
    for num in nums:
        if num == value:
            return nums.index(value)
                
  
nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = linear_search(nums, 3)
print(index) 


# print(fruits.index('bananas')) # 1

"""Begin by defining two indices: low and high. Initialize low as the lowest index in the list and high as the highest.
Loop while low is less then high.
For each iteration, calculate a third index mid which is in the middle between low and high
If the element at mid is the one you're searching for, return it, otherwise check is the target value is less than or greater than the one at mid. If it's less, make high equal to mid and loop.
If it's greater, make low equal to mid and loop. If the loop terminates without returning, return a value indicating that it was not found.
Example run:"""


