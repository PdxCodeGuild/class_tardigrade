
import pyaztro
import time
import arrow
time.sleep



    

while True:
    month = input('What is your birthmonth?: ')
    print('Calculating...')
    time.sleep(2)
    if month.lower() not in ['January', 'February', '...']:
        print('please enter a valid month...')
    else:
        break

day = int(input('What day were you born?: '))
print('*stares at the sky...')
time.sleep(2)

month_to_sign = {
    'january': [19, 'Capricorn', 'Aquarius'],
    'february': [19, 'Aquarius', 'Pisces'],
    'march': [20, 'Pisces', 'Aries'],
    'april': [19, 'Pisces', 'Taurus'],
    'may': [20, 'Taurus', 'Gemini'],
    'june': [21, 'Gemini', 'Cancer'],
    'july': [22, 'Cancer', 'Leo'],
    'august': [22, 'Leo', 'Virgo'],
    'september': [23, 'Virgo', 'Libra'],
    'october': [23, 'Libra', 'Scorpio'],
    'november': [22, 'Scorpio', 'Sagittarius'],
    'december': [21, 'Sagittarius', 'Capricorn'],
}

month_list = month_to_sign[month.lower()]
if day <= month_list[0]:
    sun = month_list[1]
else:
    sun = month_list[2]

if month == 'january' or month == 'January': # if month.lower() == 'january'
    if day <= 19:
       sun = 'Capricorn'
    elif day >20:
        sun = 'Aquarius' 
elif month == 'febuary' or month == 'Febuary':
    if day < 19:
        sun = 'Aquarius'
    elif day >= 19:
        sun = 'Pisces'
elif month == 'march' or month == 'March':
    if day <=20:
        sun = 'Pisces'
    elif day > 20:
        sun = 'Aries'
elif month == 'april' or month == 'April':
    if day <= 19:
        sun = 'Pisces'
    elif day > 19:
        sun = 'Taurus'
elif month == 'may' or month == 'May':
    if  day <= 20:
        sun = 'Taurus'
    elif day > 20:
        sun = 'Gemini'
elif month == 'june' or month == 'June':
    if day <= 21:
        sun = 'Gemini'
    elif day >21:
        sun = 'Cancer'
elif month == 'july' or month == 'July':
    if day <= 22:
        sun = 'Cancer'
    elif day > 22:
        sun = 'Leo'
elif month == 'august' or month == 'August':
    if day <= 22:
        sun = 'Leo'
    elif day > 22:
        sun = 'Virgo'
elif month == 'september' or month == 'September':
    if day <= 23:
        sun = 'Virgo'
    elif day > 23:
        sun = 'Libra'
elif month == 'october' or month == 'October':
    if  day <= 23:
        sun = 'Libra'
    elif day > 23:
        sun = 'Scorpio'
elif month == 'november' or month == 'November':
    if day <= 22:
        sun = 'Scorpio'
    elif day > 22:
        sun = 'Sagittarius'
elif month == 'december' or month == 'December':
    if day <= 21:
        sun = 'Sagittarius'
    elif day > 21:
        sun = 'Capricorn'
else:
    print('I do not understand. Please enter birthmonth and birthday')

print(f'Your Zodiac sign is {sun}!')
time.sleep(2)



traits = {'Aquarius': 'are humanitarian, independant, insightful',
'Pisces': 'are compassionate, artistic, gentle',
'Aries': 'are courageous, comfident, passionate',
'Taurus': 'are reliable, devoted, practical',
'Gemini': 'are adaptable, affectionate, curious',
'Cancer': 'are emotional, highly imaginative, persuasive',
'Leos': 'are generous, warm-hearted, creative',
'Virgo': 'are loyal, analytical, practical',
'Libra': 'are diplomatic, fair minded, social',
'Scorpio': 'are resourcful, passionate, brave',
'Sagittarius': 'are generous, idealistic, humorous',
'Capricorn': 'are disciplined, self-controled, responsible'}

matches = {'Aquarious': 'matches with Leo and Sagittarius', 
'Pisces': 'matches with Virgo and Taurus',
'Aries': 'matches with Libra and Leo',
'Taurus': 'matches with Scorpio and Cancer',
'Gemini': 'matches with Sagittarius and Aquarius',
'Cancer': 'matches with Capricorn and Taurus',
'Leo': 'matches with Aquarius and Gemini',
'Virgo': 'matches with Pisces and Cancer',
'Libra': 'matches with Aries and Sagittarius',
'Scorpio': 'matches with Taurus and Cancer',
'Sagittarius': 'matches with Gemini and Aries',
'Capricorn': 'matches with Taurus and Cancer'}

print('What else would you like to know about your sign or other signs?')
time.sleep(1)

while True:
    user_choice = input('You can choose "horoscope", "traits","matches", or "goodbye" to leave session: ')
    if user_choice == 'horoscope':
        zodiac = pyaztro.Aztro(sign=sun)
        print(zodiac.description)
    elif user_choice == 'traits':
        for trait in traits:
            if sun == trait:
                print(trait, traits[trait])
    elif user_choice == 'matches':
        for match in matches:
            if sun == match:
                print(match, matches[match])
    elif user_choice == 'goodbye':
        print('Goodbye!')  
        break  












# # import pyaztro
# taurus = pyaztro.Aztro(sign='taurus')
# taurus.description

