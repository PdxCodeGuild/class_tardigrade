nums = []

while True:
    user_input = input('Please enter your number or type done: ')
    if user_input == "done":
        
        print(nums)
        break
    else:
        nums.append(int(user_input))
        print(nums)
        
added_nums=0
for num in nums:
    added_nums = added_nums + num
    #print (added_nums)  
added_nums = added_nums/len(nums)
print(added_nums)

    
        
   
 # get user input
 # number or done
 # if user says done=break
 # if number add to nums list as int
