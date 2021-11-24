# import random

# numbers = [5, 0, 8, 3, 4, 1, 6]

# def sum(numbers):

#     total_sum = 0
    
#     for x in numbers:
#      total_sum += x
     
#     return total_sum
# result = sum(numbers)
# # print(result)


# avg = result / len(numbers)

# print(f"The average is {avg}")

    









# version 2

number_list = []

while True:
    choice = input('enter a number or "done" to finish: ')
    
    if choice == "done":
        break
        print(sum(number_list))
    else:
        choice = int(choice)
        number_list.append(choice)

def sum(numbers):

    total_sum = 0
    
    for x in numbers:
     total_sum += x
     
    return total_sum
result = sum(number_list)
print(result)

avg = result / len(number_list)

print(f'The average is {avg}')


    
