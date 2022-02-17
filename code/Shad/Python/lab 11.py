# Find: a.find(b)
# s.find(a) returns the index of a the first occurance of a

# print('hello world'.find('l'))




with open ('book.txt','r', encoding='utf-8') as b:
    book = b.read()


characters = len(book)

m = 'book.txt'


sentences = len(book.split('.' ))

words = len(book.split(' '))

# book = book.replace(' ','')
# book = book.replace('\n','')
# book = book.replace('.','')
# print(book.replace(' ',''))
# print(book.replace('\n',''))
# print(book.replace('.',''))


score = 4.71*(characters/words) + .5*(words/sentences) - 21.43
print(characters)
print(words)
print(sentences)
# print(sentences_ex, '!')
# print(sentences_ques, '?')
print(score)
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



age_14 =scale[14]['ages']
grade_14=scale[14]['grade_level']
if score  > 14:
    print(f"this book is suitable for ages {age_14} and grade level {grade_14}")
else:
    age = scale[score]['ages']
    grade=scale[score]['grade_level']
    print(f"this book is suitable for ages {age} and grade level {grade}")





   


# m = 'book.txt'





# # Counter = 1
# for letter in range(len(words)):
#     Counter+= 1
#     print(f'{Counter } {letter}')
#     print(words)
#     # print('book.txt'.find('  '))
#     # print('book.txt'.split( " "))
  