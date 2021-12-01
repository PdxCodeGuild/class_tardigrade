
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



