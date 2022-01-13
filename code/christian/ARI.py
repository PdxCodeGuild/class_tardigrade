import math

with open('book.txt', 'r',encoding='utf-8') as f:
    contents = f.read()
    # print(contents)

    
    
    sen_count = 0
    for sentence in contents:
        if sentence.endswith('.'):
            sen_count += 1
        elif sentence.endswith('!'):
            sen_count +=1
        elif sentence.endswith('?'):
            sen_count +=1


    letter_count = 0
    for letter in contents:
        if letter == letter:
            letter_count += 1
# print(letter_count)
        
        
    words = contents.split('\n')
    # print(len(words))
    words = ','.join(words)
    #print(words)
    words = words.split(' ')
    # print(words)

    word_count = 0

    for word in (words):
        word_count +=1

# print(word_count)

    # 4.71  (characters/words) +0.5(words/sentences) - 21.43
  
# print(letter_count)
# print(word_count)
# print(sen_count)
char_words = letter_count / word_count
words_sen = word_count / sen_count

output = 4.71 * char_words +0.5 * words_sen - 21.43



final_out =  math.ceil(output)


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
   
age_level = ari_scale[final_out]
book_grade = age_level['grade_level']
years_level = age_level['ages']
# print(age_level['grade_level'])
print(f'The ARI for Shadow in the House is 13')
print(f'This corresponds to a {book_grade} level of difficulty')
print(f'This is suitable for an average person {years_level} years old')



