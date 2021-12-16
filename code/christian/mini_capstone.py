
import pyaztro


    


month = input('What is your birthmonth?: ')
day = int(input('What day were you born?: '))


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
        sun = 'Aries '
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


matches = ['Leo and Sagittarius'['Virgo and Taurus']]





user_choice = input('What else would you like to know about your Zodiac? You can choose "horoscope"user "description" or "compatability.: ')

while True:
    if user_choice == 'horoscope':
        zodiac = pyaztro.Aztro(sign=sun)
        print(zodiac.description)
        break
    if user_choice == 'compatability':
        for i in matches:
            print(i)
        


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
