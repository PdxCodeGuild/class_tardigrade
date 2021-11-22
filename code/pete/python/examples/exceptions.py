"""SyntaxError"""
# print('hello')
# x = 5
# if x > 2
# print('hey')

"""IndentationError"""
# print('hello')
# x = 5
# if x > 2:
# print('hey')

# def func():
# print('this is a poorly-formatted function')

"""NameError"""
# sentence1 = 'Python is cool'
# sentence3 = 'JavaScript is cool'

# print(sentence1)
# print(sentence2)
# print(sentence3)

"""AttributeError"""
# nums = [1,2,3,4,5]
# nums.append(6)
# nums2 = '1,2,3,4,5'
# nums2.append(6)

"""TypeError"""
# var1 = 10
# var2 = '10'
# print(var1 + var2)

# colors = ['red', 'green', 'blue']
# print(colors[2.3])

"""IndexError"""
# colors = ['red', 'green', 'blue']
# for i in range(4):
#     print(colors[i])

"""KeyError"""
# test = {'a': 1, 'b': 2, 'c': 3}
# print(test['a'])
# print(test['d'])

# keys = ['a', 'b', 'c', 'd', 'e']
# for key in keys:
#     value = test.get(key)
#     if value is not None:
#         print(key, value)
#     else:
#         print('no value for ' + key)

"""ValueError"""
# print(int('1'))
# print(int('one'))

"""raising errors"""
for i in range(20):
    if i == 13:
        raise ValueError('13 is unlucky')
    print(i)