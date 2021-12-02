total = 0


while True:
     number = input("add to total or say 'done': ")
     if number == 'done':
             break
     total += int(number)
     print(f'total is currently {total}')

