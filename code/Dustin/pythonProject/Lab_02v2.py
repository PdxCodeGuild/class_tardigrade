
"""Version 2"""
print("Welcome to number averages.")
nums = []
while True:
    user_input = input("Enter numbers one at a time here, type done when done: ")
    if user_input == "done":
        break
    else:
        nums.append(int(user_input))
total = 0
for num in nums:
    total += num
total = total /len (nums)
print("The average of your numbers entered is: ")
print(total)






