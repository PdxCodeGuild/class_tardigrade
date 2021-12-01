"""Credit card validation"""

tested_num = input("enter credit card number here: ")
list_num = list(tested_num)
for i in range(0, len(list_num)):
    list_num[i] = int(list_num[i])
print(list_num)
check_num = list_num[15]

list_num = list_num[0:15:]
list_num.reverse()

print(list_num)







