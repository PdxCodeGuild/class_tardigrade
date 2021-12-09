"""
Lab 11: ARI
Author: Travis Jackson
Date: 11/29/2021

"""

import re

# open text file

path = ""

with open(path + 'oliver-twist.txt', 'r', encoding = "utf8") as book:

    content = book.read()


contents = re.sub("\n", " ", content)

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


ari = 0.0
num_char = 0
num_words = 0
num_sentences = 0


#find num char
num_char = len(re.split(".", contents))

#find number of words 
num_words = len(re.split("[^A-Za-z0-9_\-’]+", contents))


#find num sentences    check punctuation
num_sentences = len(re.split("\. ", contents))

ari = (4.71 * (num_char / num_words)) + (0.5 * (num_words/ num_sentences)) - 21.43

ari = round(ari)


if ari > 14:
    
    ari = 14

# use dictionary            
output_ages = ari_scale[ari]["ages"]
output_grades  = ari_scale[ari]["grade_level"]


# print output
print(f"The book has an ARI value of: {ari}. It is for ages {output_ages} at a {output_grades} level")
print(f"It contains {num_words} words, {num_char} characters, and {num_sentences} sentences. ")
