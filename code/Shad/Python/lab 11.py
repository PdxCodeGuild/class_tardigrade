# Find: a.find(b)
# s.find(a) returns the index of a the first occurance of a

# print('hello world'.find('l'))

from typing import Counter


characters = 302279 
words = 210420
sentences = 219
m = 'code/Shad/book.txt'

score = 4.71*(characters/words) + .5*(words/sentences) - 21.43
ari_scale = {
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
ages = [ '5-6','6-7','7-8','8-9','9-10','10-11','11-12','12-13','13-14', '14-15', '15-16','16-17', '17-18', '18-22' ]
grade=['kindergraten','First Grade', 'second grade', 'third grade', 'fouth grade', 'fifth grade','sixth grade','seventh grade', 'eight grade', 'ninth grade', 'tenth grade', 'eleventh grade', 'twelfth grade', 'college' ]
if score == 1:
    print(f' this book is suitable for ages {ages[0]} and grade {grade[0]}')
elif score == 2:
    print(f' this book is suitable for ages {ages[1]} and grade {grade[1]}')
elif score == 3:
    print(f' this book is suitable for ages {ages[2]} and grade {grade[2]}')
elif score == 4:
    print(f' this book is suitable for ages {ages[3]} and grade {grade[3]}')

elif score == 5:
    print(f' this book is suitable for ages {ages[4]} and grade {grade[4]}')
elif score == 6:
    print(f' this book is suitable for ages {ages[5]} and grade {grade[5]}')
elif score == 7:
    print(f' this book is suitable for ages {ages[6]} and grade {grade[6]}')
elif score == 8:
    print(f' this book is suitable for ages {ages[7]} and grade {grade[7]}')
elif score == 9:
    print(f' this book is suitable for ages {ages[8]} and grade {grade[8]}')
elif score == 10:
    print(f' this book is suitable for ages {ages[9]} and grade {grade[9]}')
elif score == 11:
    print(f' this book is suitable for ages {ages[10]} and grade {grade[10]}')
elif score == 12:
    print(f' this book is suitable for ages {ages[11]} and grade {grade[11]}')
elif score == 13:
    print(f' this book is suitable for ages {ages[12]} and grade {grade[12]}')
else:
    print(f' this book is suitable for ages {ages[-1]} and grade {grade[-1]}')
# with open (m,'r', encoding='utf-8') as b:
#     words = b.read()


    # print(words)
    # print(words.find('  '))
    # print(words.split( " "))
# Counter = 1
# for letter in range(len(words)):
#     Counter+= 1
#     print(f'{Counter } {letter}')
  