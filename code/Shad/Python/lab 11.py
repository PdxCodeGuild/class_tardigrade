# Find: a.find(b)
# s.find(a) returns the index of a the first occurance of a

# print('hello world'.find('l'))

from typing import Counter


characters = 302279 
words = 210420
sentences = 219
m = 'code/Shad/book.txt'

score = 4.71*(characters/words) + .5*(words/sentences) - 21.43
with open (m,'r', encoding='utf-8') as b:
    words = b.read()
print(score)

    # print(words)
    # print(words.find('  '))
    # print(words.split( " "))
# Counter = 1
# for letter in range(len(words)):
#     Counter+= 1
#     print(f'{Counter } {letter}')
  