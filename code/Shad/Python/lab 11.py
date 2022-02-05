# Find: a.find(b)
# s.find(a) returns the index of a the first occurance of a

# print('hello world'.find('l'))

from typing import Counter


characters = 302279 
words = 210420
sentences = 219
m = 'book.txt'

score = 4.71*(characters/words) + .5*(words/sentences) - 21.43
scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}
print(score)

if score == 1:
    print(' this book is suitable for ages '   + scale[1]['ages']  + ' and grades ' + scale[1]['grade_level'] )
elif score == 2:
    print(' this book is suitable for ages '   + scale[2]['ages']  + ' and grades ' + scale[2]['grade_level'] )
elif score == 3:
    print(' this book is suitable for ages '   + scale[3]['ages']  + ' and grades ' + scale[3]['grade_level'] )
elif score == 4:
    print(' this book is suitable for ages '   + scale[4]['ages']  + ' and grades ' + scale[4]['grade_level'] )

elif score == 5:
    print(' this book is suitable for ages '   + scale[5]['ages']  + ' and grades ' + scale[5]['grade_level'] )
elif score == 6:
    print(' this book is suitable for ages '   + scale[6]['ages']  + ' and grades ' + scale[6]['grade_level'] )
elif score == 7:
    print(' this book is suitable for ages '   + scale[7]['ages']  + ' and grades ' + scale[7]['grade_level'] )
elif score == 8:
    print(' this book is suitable for ages '   + scale[8]['ages']  + ' and grades ' + scale[8]['grade_level'] )
elif score == 9:
    print(' this book is suitable for ages '   + scale[9]['ages']  + ' and grades ' + scale[9]['grade_level'] )
elif score == 10:
    print(' this book is suitable for ages '   + scale[10]['ages']  + ' and grades ' + scale[10]['grade_level'] )
elif score == 11:
    print(' this book is suitable for ages '   + scale[11]['ages']  + ' and grades ' + scale[11]['grade_level'] )
elif score == 12:
    print(' this book is suitable for ages '   + scale[12]['ages']  + ' and grades ' + scale[12]['grade_level'] )
elif score == 13:
    print(' this book is suitable for ages '   + scale[13]['ages']  + ' and grades ' + scale[13]['grade_level'] )
else:
    print(' this book is suitable for ages '   + scale[14]['ages']  + ' and grades ' + scale[14]['grade_level'] )
with open (m,'r', encoding='utf-8') as b:
    words = b.read()


    print(words)
    print(words.find('  '))
    print(words.split( " "))
Counter = 1
for letter in range(len(words)):
    Counter+= 1
    print(f'{Counter } {letter}')
  