import string
import re
import math #got from "geeksforgeeks.org as well as math.ceil() function in order to round up ari math result"
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

s = re.findall("[\.?!]", contents)
sentences= float((len(s)))
characters_total=float(characters_total)
word_count=float(word_count)
ari_not_complete=(((characters_total/word_count)*4.71)+((word_count/(sentences))*.5)-21.43)
ari = math.ceil(ari_not_complete)
print(f"The ARI for {title} is {ari}")


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

if ari in ari_scale:
    print(f"This corresponds to a {ari_scale[ari]['grade_level']} level of difficulty that is suitable for an average person {ari_scale[ari]['ages']} years old.")
    if ari > 14:
        print(f"This corresponds to a {ari_scale[ari]['grade_level']} level of difficulty that is suitable for an average person {ari_scale[ari]['ages']} years old.")
