import string
import re

with open('vanessa\kidnapped.txt', 'r',encoding='utf-8') as kidnapped:
    contents = kidnapped.read()
title="Kidnapped"
characters_total= 0
for character in contents:
    if character in string.ascii_letters:
        characters_total= characters_total +1
# print (f"characters total: {characters_total}")

words=contents.split()
word_count = 0
for word in words:
    word_count += 1
# print(f"word count {word_count}")

x = re.findall("[\.?!]", contents)
# print(len(x))
characters_total=float(characters_total)
totals=4.71(characters_total/word_count)
print(totals)
first_part=(characters_total/word_count) 
second_part=(word_count/len(x))
first_part2= first_part*4.71
second_part2= second_part*0.5
total=(first_part2 + second_part2)-21.43
x=total//1
print(f"The ARI for {title} is {x}")
#7.0333

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

if x in ari_scale:
    print(f"This corresponds to a {ari_scale[8]['grade_level']} level of difficulty that is suitable for an average person {ari_scale[8]['ages']} years old.")



# {book['title']} by {book["author"]}                                   
# This corresponds to a 11th Grade level of difficulty
# that is suitable for an average person 16-17 years old.