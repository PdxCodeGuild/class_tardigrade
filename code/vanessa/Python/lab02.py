#add to each other, then divide by length

nums = [5, 0, 8, 3, 4, 1, 6]

added_nums=0
for num in nums:
    added_nums = added_nums + num
    #print (added_nums)  
added_nums = added_nums/len(nums)
print(added_nums)
   

    
'''  
for i in range(len(nums)):
    print(nums[i])
    added_nums = added_nums + nums[i]
    #added_nums.append([i])
    / len(added_nums)
    print (sum(added_nums))'''