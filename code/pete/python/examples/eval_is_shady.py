secret_key = '12345hahanobodywillknow!'

print('welcome to the calculator')
equation = input('enter your equation: ')
result = eval(equation)

print(f'the answer to {equation} is {result}')