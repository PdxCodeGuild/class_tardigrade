# convert numbers to words

# fruits = {'kiwi': 'green', 'orange': 'orange', 'peach': 'light orange'}
# print(fruits['kiwi'])


number_word = {
    'dog': 'white', 
    'cow': 'orange', 
    'zebra': 'grey',
    'giraffe':'yellow',
    'bear': 'black'
    }
print(number_word['cow'])

ones_dict = {
    1: 'one',
    2: 'two'
}

tens_dict = {
    1: 'ten',
    2: 'twenty',
    3: 'thirty',
    4: 'fourty'
    
}

x = input('eneter a number')
x = int(x)
tens_digit = x//10 # floor division
ones_digit = x%10 # modles
# print(tens_digit, ones_digit)
if x < 20:
    print(f'{tens_dict[tens_digit]}, {ones_dict[ones_digit]} ')

else: 
    print(tens_dict[tens_digit])
    print(ones_dict[ones_digit])

    print(f'{tens_dict[tens_digit]}, {ones_dict[ones_digit]} ')


# unfinished lab