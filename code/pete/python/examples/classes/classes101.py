# everything has a class
# every object has a class
print(type(1), type('hello world'))

numbers = [1, 2, 3, 4, 5]
# diffent classes have different properties
numbers.append(2) # .append is a method of the list class, every list has the .append method

message = 'hello world'
# strings have different methods than lists
message.capitalize() # .capitalize is a method of the string class, every string has the .capitalize method


# object-oriented programming is a paradaigm of programming, where you focus on creating and using objects