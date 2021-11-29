# credit card validation lab

# 
input : 4972038308547166
output : 498749745497454
Credit_card = int(input('enter credit number:'))

sum1=3
sum2=3

# 
while Credit_card != 0:
    sum1 += Credit_card % 10
    Credit_card = Credit_card // 100

#

# sum2 

# while Credit_card != 0:
#     n = Credit_card % 100
#     n = n // 10
#     n = n * 2
#     sum2 += n//10 + n%10
#     Credit_card = Credit_card // 100
    
print(sum1, sum2)