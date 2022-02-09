

user = int(input('Enter your number  '))
single = {1:"one", 2:'two', 3:'three',4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9: 'nine'}
teen =  {11:"eleven", 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19: 'nineteen'}
two = {1:"ten", 2:'twenty', 3:'thirty',4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9: 'ninety'}
hun = {1:"one hundred", 2:'two hundred', 3:'three hundred',4:'four hundred', 5:'five hundred', 6:'six hundred', 7:'seven hundred', 8:'eight hundred', 9: 'nine hundred'}
teens= teen.get(user)
hundred = user//100
tens = user//10%10
ones = user%10
teeen = user%100
# print(hundred)

# print(ones)



# if user < 10:
#     print(f'{single.get(ones)}')
# elif user > 10 and user > 19 and user <= 99:
#     print(f'{two.get(tens)} {single.get(ones)}' )
# elif user >= 100:
#     print(f'{hun.get(hundred)} {teen.get(teeen)} {two.get(tens)} {single.get(ones)}' )
# elif user >= 110:
#     print(f'{hun.get(hundred)} {teen.get(teeen)}  {two.get(tens)} {single.get(ones)}')

if user >= 100 and user <= 110:
    print(f'{hun.get(hundred)}  {single.get(ones)}' )
elif user == 10:
    print(f'{two.get(tens)}')

elif user > 110 and user <= 119:
    print(f'{hun.get(hundred)} {teen.get(teeen)}' ) 

elif user > 110 and user < 120:
    print(f'{hun.get(hundred)} {teen.get(teeen)}' )

elif user >= 119 and user == 121 :
    print(f'{hun.get(hundred)} {two.get(tens)} {single.get(ones)}' )
elif user >= 120:

    print(f'{hun.get(hundred)} {two.get(tens)} ' )

    


elif user > 10 and user < 20:
    print(f'{teen.get(teeen)} ' )
elif user > 19 and user <= 99:
    print(f'{two.get(tens)}' )
elif user > 10 and user > 19 and user <= 99:
    print(f'{two.get(tens)} {single.get(ones)}' )
elif user > 10 or user < 20:
    print(teen.get(teeen))
elif user < 10:
    print(f'{single.get(ones)}')


else:
    print(f'{hun.get(hundred)} + {teeen}' )



