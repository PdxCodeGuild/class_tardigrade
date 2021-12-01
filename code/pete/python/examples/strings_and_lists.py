"""Looping"""
integers = [1,2,3,4,5]
for integer in integers:
    print(integer)

message = 'coding is fun'
for letter in message:
    print(letter)


"""Access"""
print(integers[3])
print(message[3])


"""Assignment"""
integers[3] = 7
print(integers)
# message[3] = 'I' # TypeError 'str' object does not support item assignment


"""Appending vs. Concatenation"""
integers.append(9)
print(integers)
message += '!' # same thing as message = message + '!'
print(message)