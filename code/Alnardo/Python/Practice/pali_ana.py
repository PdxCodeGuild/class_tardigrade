#Palindrome

# txt = "Hello World"[::-1]
# print(txt)
"""
word = input('Please enter a word: ').lower()
word2 = word[::-1]
print(word2)
def check_pali():
    if word == word2:
        return print(f'{word} is a palindrome!')
    else:
        return print(f'{word} is not a palindrome... Try again later!')

check_pali()

"""#Anagram

inputted_word_1 = input('What is your first word?: ')
inputted_word_2 = input('What is your second word?: ')

word_1 = inputted_word_1
word_2 = inputted_word_2

inputted_word_1 = list(inputted_word_1)
inputted_word_2 = list(inputted_word_2)

# print(inputted_word_1)
# print(inputted_word_2)
# print(sorted(inputted_word_1))

inputted_word_1.sort()
inputted_word_2.sort()
# print(inputted_word_1)
# print(inputted_word_2)


if inputted_word_1 == inputted_word_2:
    print(f'{word_1} and {word_2} are anagrams!')
else: 
    print(f'{word_1} and {word_2} are not anagrams.')
