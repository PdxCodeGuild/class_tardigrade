code=[]

rot13 = {'a':'n', 'b':'o','c':'p','d':'q','e':'r','f':'s','g':'t','h':'u','i':'v','j':'w','k':'x','l':'y','m':'z','n':'a','o':'b','p':'c','q':'d','r':'e','s':'f','t':'g','u':'h','v':'i','w':'j','x':'k','y':'l','z':'m'} 
user = input('Enter your string: ')
for i, co in enumerate(user):
    if True:
        i=rot13.get(user[i])
    print(i, end=' ')


# rot13.get(user)
