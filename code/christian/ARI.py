

with open('book.txt', 'r',encoding='utf-8') as f:
    contents = f.read()
    # print(contents)

    
    
    sen_count = 0

    for sentence in contents:
        if sentence.endswith('.'):
            sen_count += 1
        elif sentence.endswith('!'):
            sen_count +=1

print(sen_count)
        

    
    
    
    
    
#     letter_count = 0
#     for letter in contents:
#         if letter == letter:
#             letter_count += 1
# print(letter_count)
        
        
    
    
    # words = contents.split('\n')
    # # print(len(words))
    # words = ','.join(words)
    # #print(words)
    # words = words.split(' ')
    # print(words)

#     word_count = 0

#     for word in (words):
#         word_count +=1

# print(word_count)

    
  



    


        


