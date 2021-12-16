#  Creating a graphing calculator in python
#  Plugging in an equation and getting its graph back
#  numpy 1.21.4 installed in C:\Users\Alnar\AppData\Local\Programs\Python\Python310\Scripts
#  MATPLOTLIB  cycler-0.11.0 fonttools-4.28.3 kiwisolver-1.3.2 matplotlib-3.5.0 packaging-21.3 pillow-8.4.0 pyparsing-3.0.6 python-dateutil-2.8.2 setuptools-scm-6.3.2 six-1.16.0 tomli-1.2.2 installed


import matplotlib.pyplot as plt
print('*-*'*20)
print('\n\tWelcome to the Graphing Calculator!\n')
print('*-*'*20)


x1_min = int(input('Please enter the minimum x value: '))
x2_max = int(input('Please enter the maximum x value: '))

min_max = range(x1_min, x2_max)

y=[]

expr = input('Please enter an equation: ')

for x in min_max:
    answer = eval(expr) 
    y.append(answer)
# print(y)

mean = 0
counter = 0
question = input('Would you like to calculate the median and/or mean? (yes/no): ')
while question == 'yes':
    choice_1 = input('Would you like the mean?: ')
    for j in y:
        mean += j
        counter += 1
    if choice_1 == 'yes':
        average = mean / counter
        print(average)
    choice_2 = input('Would you like the median?: ')
    if choice_2 == 'yes':
        median = 0
        if counter % 2 == 0:
            median = int(counter/2)
            median = y[median]
            print(median)
        elif counter % 2 == 1:
            x1 = counter // 2
            x2 = (counter // 2) + 1
            median = (y[x1] + y[x2]) / 2
            print(median)
    break


marker_options = ['.', ',', 'o', 'v', '^', 'x', '<', '>', '1', '2', '3', '4', '8', 's', 'p', 'P', 'd', 'D', 'X']
color_options = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
while True:
    marker_choice = input('What kind of marker would you like to use? (Enter "options" for a list of available choices): ')
    if marker_choice == 'options':
        print(marker_options)
    elif marker_choice not in marker_options:
        print('Invalid choice')
    else:
        break
while True:
    color_choice = input('What kind of color would you like to use? (Enter "options" for a list of available choices): ')
    if color_choice == 'options':
        print(color_options)
    elif color_choice not in color_options:
        print('Invalid choice')
    else:
        break


# print(marker_choice)
# linestyle='dashed'
# plt.hlines(y=0, xmin=-5, xmax=20, linewidth=4, color='r')
plt.plot(min_max, y, color=color_choice, marker=marker_choice, linewidth=2, markersize=8) 

plt.title(f'{expr}')


plt.show()