# Need to create an equation using inputs...

# from sympy import symbols
import matplotlib.pyplot as plt
import numpy as np
# x = symbols('x')

# x1_min = 1
# x2_max = 6

# rang=range(x1_min, x2_max)

# y=[]

# expr = input('Please enter an equation: ')

# for x in rang:
#     f = eval(expr)
#     y.append(f)
# print(y)

    # y.append((i+2)+3)

tan = np.tan
sin = np.sin
cos = np.cos

# x = 0
# print(answer)
# sohcahtoa = input("Please enter sin, cos, or tan?: ")
# answer_2 = getattr(np, sohcahtoa)
num_1 = int(input('Please enter the minimum number for x: '))
num_2 = int(input('Please enter the maximum number for x: '))
x = np.arange(num_1*np.pi,num_2*np.pi,0.1)   # start,stop,step
test = input('Enter your trig equation: ')
answer = eval(test)
y = answer
z = np.sin(x)
plt.plot(x, y, x, z)
plt.show()