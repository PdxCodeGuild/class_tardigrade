
import pyaztro
import time
import arrow
time.sleep



    


month = input('What is your birthmonth?: ')
print('Calculating...')
time.sleep(2)

day = int(input('What day were you born?: '))
print('*stares at the sky...')
time.sleep(2)

if month == 'january' or month == 'January':
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

# Aries	March 21 -April 19	Energetic, candid and willful
# Taurus	April 20 - May 20	Reliable, diligent and conservative
# Gemini	May 21 - June 21	Quick-witted, capricious and cheerful
# Cancer 	June 22 - July 22	Considerate, imaginative and sensitive
# Leo 	July 23 - August 22	Enthusiastic, proud and arrogant
# Virgo  	August 23 - September 22	Elegant, perfectionist and picky
# Libra 	September 23 - October 23	Equitable, charming and hesitant
# Scorpio 	October 24 - November 22	Insightful, mysterious and suspicious
# Sagittarius	November 23 - December 21	Unconstrained, lively and rash
# Capricorn 	December 22 - January 19	Perseverant, practical and lonely
# Aquarius	January 20 - February 18	Smart, liberalistic and changeful
# Pisces	February 19 - March 20	Romantic, kind and sentimental
