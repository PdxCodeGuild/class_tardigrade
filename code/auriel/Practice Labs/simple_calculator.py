while True:
    operation = input('What operation would you like to perfom (use symbol). Type done to quit: ').lower()
    num1 = float(input('What is the first number: '))
    num2 = float(input('What is the second number: '))

    if operation == '+':
        total = num1 + num2
        print(f'{num1} + {num2} = {total}')
    if operation == '-':
        total = num1 - num2
        print(f'{num1} - {num2} = {total}')
    if operation == '*':
        total = num1 * num2
        print(f'{num1} * {num2} = {total}')
    if operation == '/':
        total = num1 / num2
        print(f'{num1} / {num2} = {total}')
    if operation == 'done':
        break
    else:
        print('Please select one of these operations + / * -')