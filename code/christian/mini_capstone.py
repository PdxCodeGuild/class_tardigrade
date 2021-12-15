import astropy
from astropy import time
import arrow
import pyaztro



month = input('What is your birthmonth?: ')
day = int(input('What day were you born?: '))

if month == 'january' or month == 'January':
    if day < 20:
        print('Your sun sign is Capricorn!')
    elif day >= 20:
        print('Your sun sign is Aquarius!') 
if month == 'febuary' or month == 'Febuary':
    if day < 19:
        print('Your sun sign is Aquarius!')
    elif day >= 19:
        print('Your sun sign is Pisces!')
if month == 'march' or month == 'March':
    if day <=20:
        print('Your sun sign is Pisces!')
    elif day > 20:
        print('Your sun sign is Aries! ')
if month == 'april' or month == 'April':
    if day <= 19:
        print('Your sun sign is Pisces')
    elif day > 19:
        print('Your sun sign is Taurus!')
if month == 'may' or month == 'May':
    if  day <= 20:
        print('Your sun sign is Taurus!')
    elif day > 20:
        print('Your sun sign is Gemini!')
if month == 'june' or month == 'June':
    if day <= 21:
        print('Your sun sign is Gemini!')
    elif day >21:
        print('Your sun sign is Cancer!')
if month == 'july' or month == 'July':
    if day <= 22:
        print('Your sun sign is Cancer!')
    elif day > 22:
        print('Your sun sign is Leo!')
if month == 'august' or month == 'August':
    if day <= 22:
        print('Your sun sign is Leo!')
    elif day > 22:
        print('Your sun sign is Virgo!')
if month == 'september' or month == 'September':
    if day <= 23:
        print('Your sun sign is Virgo!')
    elif day > 23:
        print('Your sun sign is Libra!')
if month == 'october' or month == 'October':
    if  day <= 23:
        print('Your sun sign is Libra!')
    elif day > 23:
        print('Your sun sign is Scorpio!')
if month == 'november' or month == 'November':
    if day <= 22:
        print('Your sun sign is Scorpio!')
    elif day > 22:
        print('Your sun sign is Sagittarius!')
if month == 'december' or month == 'December':
    if day <= 21:
        print('Your sun sign is Sagittarius!')
    elif day > 21:
        print('Your sun sign is Capricorn!')
else:
        print('I do not understand. Please enter birthmonth and birthday')

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
