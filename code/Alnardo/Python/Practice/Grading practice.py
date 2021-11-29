#Grading Practice Lab

grade = input('Enter the grade: ')
grade = int(grade)

if grade >= 90 and grade <= 100:
    print('Congrats, you got an A!')

elif grade >= 80 and grade <= 89:
    print('Congrats, you got a B!')

elif grade >= 70 and grade <= 79:
    print('You got a C, you pass!')

elif grade >= 60 and grade <= 69:
    print('You got a D, needs more work.')

elif grade >= 0 and grade <= 59:
    print('You got an F, did you even try?')

#A+ etc..

grade = input('Enter the grade: ')
grade = int(grade)

supplement = {
    0 : '-',
    1 : '-',
    2 : '-',
    3 : '-',
    4 : '',
    5 : '',
    6 : '',
    7 : '+',
    8 : '+',
    9 : '+'
}
add_on = grade % 10
add_on = supplement[add_on]

print(add_on)

if grade == 100:
    print('Congrats, you got an perfect score!')

elif grade >= 90 and grade < 100:
    print(f'Congrats, you got an A{add_on}!')

elif grade >= 80 and grade <= 89:
    print(f'Congrats, you got a B{add_on}!')

elif grade >= 70 and grade <= 79:
    print(f'You got a C{add_on}, you pass!')

elif grade >= 60 and grade <= 69:
    print(f'You got a D{add_on}, needs more work.')

elif grade >= 0 and grade <= 59:
    print('You got an F, did you even try?')

else:
    print('A grade outside of 0-100 is invalid. What are you doing?!')