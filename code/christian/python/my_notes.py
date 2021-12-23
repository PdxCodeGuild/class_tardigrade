fruits = ['grapes', 'apples', 'pears', 'oranges', 'kiwis'] 
colors = ['red', 'blue', 'green']
# for i in range(len(fruits)):
    # print(fruits[i])


def demonstration(cat):
    print(cat)


# demonstration(fruits)

def myfunc(bear, lion):
    for x in (bear):
        print(x,'elements of bear list')
    output = len(lion)
    print(output, 'length of lion list')

myfunc(colors, fruits)


#enumerate in for loop 

card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


for i, x in enumerate(card): #enumerate loops through element and indicies(i) at the same time
    if x > 4:
        card[i] -= 1 #can be used to manipulate lists with less code vs basic for loop






#ROT with dictionary


def encode (message):
        rot13 = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u',
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',   #dictionary with 13 moves of letters
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m',}
        input = " " 
        for x in message: #for loop to add dictionary to variable
         input = input + rot13.get(x)  # use .get to access key value
         print(input)

# print(encode('hello'))


user_message = input('What would you like to encode?: ')

(encode(user_message))



with open('book.txt', 'w') as book_file:
    book_file.write('hello')   #used to write over book, is in contacts lab
