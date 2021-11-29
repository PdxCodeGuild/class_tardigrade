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