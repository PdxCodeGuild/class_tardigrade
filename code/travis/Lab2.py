"""
Lab 2
Author:" Travis Jackson
Date: 11/16/21

"""


nums = [5, 0, 8, 3, 4, 1, 6]
nums2 = []

sum = 0
sum2 = 0

average = 0
average2 = 0

for num in nums:
    sum = num + sum

average = sum / len(nums)

print("The average of the list is:", average)


# Version 2


while True:
    num_input = input("Enter a number, or 'done': ")
    
    if num_input == "done":
        for num2 in nums2:

            sum2 = num2 + sum2
        average2 = sum2 / len(nums2)

        print("The average is:", average2)
        break

    nums2.append(int(num_input))





