# credit card validation lab

# 
input : 4972038308547166
output : 498749745497454
Credit_card = int(input('enter credit number:'))

sum1=1
sum2=2

# 
while Credit_card != 0:
    sum1 += Credit_card % 10
    Credit_card = Credit_card // 100

#


print(sum1, sum2)

# unfinished lab