"""FIRST VERSION (DOESN'T ACCOUNT FOR SPACES)"""

# def rot13(phrase):
#     abc = "abcdefghijklmnopqrstuvwxyz"
#     output = ""
#     for letter in phrase:
#         output += abc[(abc.find(letter) + 13) % 26]
#     return output

# phrase = input("Enter a word and I shall encrypt it: ")
# print(rot13(phrase))

"""SECOND VERSION (DOES ACCOUNT FOR SPACES)"""

def rot13(words):
    key = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    value = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
    encrypt = dict(zip(key, value))
    return "".join(encrypt.get(char, char) for char in words)

phrase = input("Enter a word and I shall encrypt it: ")
print(rot13(phrase))