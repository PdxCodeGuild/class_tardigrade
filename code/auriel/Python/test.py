
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cipher():
    user = input('Please input a phrase: ')
    phrase = list(user)
    coded = []

    for i, letter in enumerate(phrase):
        for l, alpha in enumerate(lowercase_letters):
            if letter == alpha and letter < lowercase_letters[13]:
                coded.append(lowercase_letters[l + 13])
            if letter == alpha and letter > lowercase_letters[12]:
                coded.append(lowercase_letters[l - 13])

    final_output = ''.join(coded)
    print(final_output)
    
cipher()