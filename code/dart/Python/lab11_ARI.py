import math
import string

file_path = "/Users/dartagnanchilders/Desktop/pdx_code/FS_bootcamp/class_tardigrade/code/dart/"

with open(file_path + "great_leaders.txt", 'r') as f:
    book_data = f.read()

def character_counter(x):
    char_num = book_data.replace(" ", "")
    char_num = book_data.replace("\n", "")
    for i in string.punctuation:
        char_num = book_data.replace(i, "")
    char_num = len(char_num)
    return char_num

def word_counter(x):
    word_num = book_data.split(" ")
    word_num = len(word_num)
    return word_num

def sentence_counter(x):
    sen_num = book_data.replace("!", ".")
    sen_num = book_data.replace("?", ".")
    sen_num = book_data.split(".")
    sen_num = len(sen_num)
    return sen_num

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

def ari(x):
    char_num = character_counter(x)
    word_num = word_counter(x)
    sen_num = sentence_counter(x)
    ari_score = math.ceil((4.71 * (char_num / word_num)) + (0.5 * (word_num / sen_num)) - 21.43)
    if ari_score > 14:
        ari_score = 14
    return ari_score
i = ari(book_data)

print(f"The ARI for \"Great Leaders\" is {i}. \nThis corresponds to a \
{ari_scale[i]['grade_level']} level of difficulty. \nThat is suitable for an \
average person {ari_scale[i]['ages']} years old.")
