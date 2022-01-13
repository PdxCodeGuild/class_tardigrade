with open('book.txt') as file:
    lines = file.read().split('\n')
# print(lines)

characters = 0
# print(lines)
# print(hello[0])
# print(len(lines))
# print(type(lines))
strlines = (' '.join(lines))
word_list = strlines.split()
# words = strlines.split(' ')
# print(word_list)
word_counts = len(word_list)
print(word_counts)
