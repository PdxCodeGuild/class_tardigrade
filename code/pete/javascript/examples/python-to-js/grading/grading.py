# prompt: give me a percentage grade
# user types in 85
# program says they got a B

percentage = int(input('enter a percentage grade: '))

if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"You got a{'n' if grade == 'A' else ''} {grade}.")

# number = 2
# # python oneline conditional
# even_or_odd = 'even' if number % 2 == 0 else 'odd'

# if number % 2 == 0:
#     even_or_odd = 'even'
# else:
#     even_or_odd = 'false'

# def add(a, b):
#     return a + b

# print(a, b)


var1 = 1
var2 = '2'
print(var1 + var2)