nums = [5, 0, 8, 3, 4, 1, 6]
running_sum = 0
t = len(nums)

for num in nums:

    running_sum = running_sum + num
    print(num, "elements in nums list")
    print(running_sum)
#end for loop
result = running_sum/t
print(result)


