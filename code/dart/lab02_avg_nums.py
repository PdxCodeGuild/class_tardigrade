""" VERSION 1 """

# nums = [8, 6, 7, 5, 3, 0, 9]

# avg = round(statistics.mean(nums), 2)
# print(f"The average of {nums} is {avg}.")

""" VERSION 2 """

def calculated_average(nums):
    sum_num = 0
    for i in nums: 
        sum_num += i

    average = sum_num / len(nums)
    return average 

nums = []

while True:
    user_input = input("Enter a number or type \"done\" to quit: ")
    if user_input == "done":
        print(f"The average is {round(calculated_average(nums), 2)}")
        break
    else:
        nums.append(int(user_input))
        avg = round(calculated_average(nums), 2)


