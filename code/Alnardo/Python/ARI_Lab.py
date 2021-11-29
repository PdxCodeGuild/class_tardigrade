#ARI Lab(Not Alcohol)
# import math
text = 'Raven.txt'

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


# pathing = 'github\class_tardigrade\code\Alnardo\Python\Beowulf.txt'
character_count = 0
sentence_counter = 0
word_counter = 0
with open('Raven.txt', 'r', encoding='utf-8') as f:
    # text = f.read()

    lines = f.read().split('\n')
    # print(lines)
    for sentence in lines:
        sentence_counter += 1
        # print(sentence)
    print(sentence_counter)
    # print(character_count)

    lines = ' '.join(lines)
    lines = lines.split()
    # print(lines)
    for i, word in enumerate(lines):
        # print(i, word)
        word_counter += 1
        for character in word:
            # print(character)
            character_count += 1
    print(character_count)
    print(word_counter)
    # print(lines)
        # if sentence == '':
        #     lines.remove(sentence)
        # for ind, character in enumerate(sentence):
            # print(character)
            # character_count += ind
            # print(ind)
    # print(character_count)

ari_score = int((4.71*(character_count/word_counter) + 0.5*(word_counter/sentence_counter) -21.43) // 1 + 1)
# ari_score = math.ceil(ari_score)
print(ari_score)
print(ari_scale[ari_score])
age = ari_scale[ari_score]['ages']
# print(age)
grade_level = ari_scale[ari_score]['grade_level']
# print(grade_level)

print(f'The ARI score for {text} is {ari_score}!\nThis corresponds to a {grade_level} level of difficulty,\nthat is suitable for {age} years old.')




