# credit card validation lab

# 
# input : 4972038308547166
output : 498749745497454
Credit_card = input('enter credit number:')

sum1=1
sum2=2

card_numbers = "4972038308547166"
card_numbers = list(card_numbers)


num_list = []

for num in card_numbers:
    num = int(num)
    num_list.append(num)
# print(card_numbers)

lastnum = num_list.pop()
num_list.reverse()
print(num_list)
counter = 0
for num in num_list:
    counter += 1
    if counter %2 == 0:
       num += num
       num_list[counter]=num
print(num_list)
