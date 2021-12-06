mylist = ['A', 'B', 'C', 'D', 'E',
        'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O',
        'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y', 'Z']


letters = input('enter a letter here').upper()
word_letters = ""
for i in letters:
    index = mylist.index(i)
    if index > 13:
        word_letters += mylist[index-13]
    else:
        
        word_letters += mylist[index+13]
print(word_letters)





