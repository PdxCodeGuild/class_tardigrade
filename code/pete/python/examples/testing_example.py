def all_3s(text):
    for letter in text:
        if letter != '3':
            return False
    return True


print(all_3s('333333'))
print(all_3s('3353333'))

message = input('give a message to test the all_3s function: ')
print(all_3s(message))