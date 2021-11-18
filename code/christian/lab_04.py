# # number to word conversion via dictionary

ones = {0:'zero',
 1:'one',
  2:'two',
   3:'three',
   4:'four',
   5:'five',
   6:'six',
   7:'seven',
   8:'eight',
   9:'nine',}

teens = {10:'ten',
11:'eleven',
12:'twelve',
13:'thirteen',
14:'fourteen',
15:'fifteen',
16:'sixteen',
17:'seventeen',
18:'eighteen',
19:'nineteen'}

tens = {2:'twenty',
3:'thirty',
4:'forty',
5:'fifty',
6:'sixty',
7:'seventy',
8:'eighty',
9:'ninety'}

# hundreds = {1: 'one hundred',
# 2: 'two hundred',
# 3: 'three hundred',
# 4: 'four hundred',
# 5: 'five hundred',
# 6: 'six hundred',
# 7: 'seven hundred',
# 8: 'eight hundred',
# 9: 'nine hundred'}



 


choice =  int(input('chose a number to convert between 0-99: '))

tens_con = choice // 10
ones_con = choice % 10




if 0 < choice and choice < 10:
    print(ones[choice])
      
elif choice >= 10 and choice < 20:
    print(teens[choice])
elif choice > 19:
    if ones_con == 0:
        print(tens[tens_con])
    else:
     print(f'{tens[tens_con]}-{ones[ones_con]}')
    
    
    # print(tens[tens_con])
    # print(ones[ones_con])

    
    
    # print(tens_con)

    # print(ones_con)
    
    # if choice > 100 and choice < 1000:
#     print (ones[choice] + 'hundred')  
   
     







# extract tens place using //10
# access tens dictionary
# then access ones place
# then concatinate the value from tens dictionary with value from ones dictionary

# x = 67
# tens_digit = x//10
# ones_digit = x%10
# print(choice % 10)


# floor divided by 10 gets 10th place
# % divided by 10 gets ones place