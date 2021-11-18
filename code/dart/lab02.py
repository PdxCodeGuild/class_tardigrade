import statistics

""" VERSION 1 """

# nums = [8, 6, 7, 5, 3, 0, 9]

# avg = round(statistics.mean(nums), 2)
# print(f"The average of {nums} is {avg}.")

""" VERSION 2 """

nums = []

while True:
    user_input = input("Enter a number or type \"done\" to quit: ")
    if user_input == "done":
        print(f"The average of {nums} is {avg}.")
        break
    else:
        nums.append(int(user_input))
        avg = round(statistics.mean(nums), 2)
