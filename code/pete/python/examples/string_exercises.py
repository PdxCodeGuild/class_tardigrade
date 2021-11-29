# """String Literals"""
# print("strings can have double quotes")
# print('strings can have single quotes')
# print('you can use "double quotes" inside single quotes')
# print("you can use 'single quotes' in side double quotes")
# print('hèłłô wörłd')

# """Escape Sequences"""
# print('say \'hello\'')
# print('things to do\n\tlearn python\n\tlearn javascript')
# print(r'things to do\n\tlearn python\n\tlearn javascript')
# print('backslash \\')
# # unicode characters '\uxxx'
# print('\u0393')
# print('\u0394')
# print('\u0395')
# print('\u2495')
# print('\u0000')
# print('\u0002')
# print('\u0003')
# print('\u0013')
# print('\u0113')
# print('\u4113')

# """ord() and chr()"""
# # ord takes a character and returns the integer of its ascii code
# from string import ascii_letters
# for letter in ascii_letters:
#     print(letter, ord(letter))
# # char takes an integer and returns the corresponding character
# for i in range(400):
#     print(i, chr(i))


"""Concatenation & Multiplication"""
message = 'hello'
message = message + ' ' + 'world'
message += '!'
for i in range(40):
    print(i)
print('\n' + '*'*40)
print(message)
print('*'*40 + '\n')
for i in range(40):
    print(i)


"""Access: string[i]"""
school = 'PDXCodeGuild'
# using bracket notation, print out the 'X' in 'PDXCodeGuild'
print(school[2])
# school[2] = 'x' TypeError: 'str' object does not support item assignment

"""Slicing: string[i:j:k]"""
# using bracket notation, print out the 'Code' from 'PDXCodeGuild'
print(school[3:7])

"""String Methods"""
print('test'.find('e')) # 1
print('test'.find('st')) # 2

# loop over this list, and use string.startswith() and string.endswith()
# to make sure that every sentence is exactly like this: 'Coding is fun.'
# use string.capitalize() and concatenation to replace any strings
sentences = [
    'Coding is fun.', # 0
    'Coding is fun',  # 1
    'Coding is fun.', # 2
    'coding is fun.', # 3
    'coding is fun',  # 4
    'Coding is fun',  # 5
]
print(set(sentences))
# list[number]
for i, sentence in enumerate(sentences):
    # print('\n' + sentence)
    # print(i)
    # sentence = sentence.capitalize()
    # print(sentence)
    # if sentence.endswith('.') == False:
    if not sentence.endswith('.'):
        sentence = sentence + '.'
    sentences[i] = sentence.capitalize()
    print(sentence)

print(sentences)
print(set(sentences))

"""Strip"""
print('    hello\n')
print('    hello\n'.strip())

print('@@@the@message@is@here@@@')
print('@@@the@message@is@here@@@'.strip('@'))

print(')(*&^here is the message%$#@!'.strip(')(*&^%$#@!'))


"""Split and Join"""
students = 'shad, auriel, travis, dustin, christian, alnardo, vanessa, lujock'

# use string.split() to split the student names into a list
students = students.split(', ')

# sort the names alphabetically
students.sort()

# use string.join(list) to get a new string of the sorted names
students = ', '.join(students)

"""not official python! don't do it like this"""
# students.join(', ') # pete wants it to be this way

print(students)

"""F-Strings"""
print('my favorite number is ' + str(1))
print(f'my favorite number is {1}') # no need to type convert


"""string in string"""
print('h' in 'hello world') # True if character in string
print('hel' in 'hello world') # True if substring in string
print('helo' in 'hello world') # False if substring not in string

"""Looping Over Strings"""
for letter in 'abcde':
    print(letter)

"""Docstrings"""
def add(x, y):
    """adds x and y and returns that value"""
    return x + y

add(1, 2)