#  Creating a graphing calculator in python
#  Plugging in an equation and getting its graph back
#  numpy 1.21.4 installed in C:\Users\Alnar\AppData\Local\Programs\Python\Python310\Scripts
#  MATPLOTLIB  cycler-0.11.0 fonttools-4.28.3 kiwisolver-1.3.2 matplotlib-3.5.0 packaging-21.3 pillow-8.4.0 pyparsing-3.0.6 python-dateutil-2.8.2 setuptools-scm-6.3.2 six-1.16.0 tomli-1.2.2 installed
import matplotlib.pyplot as plt
x=range(0,9)
y=[]
for i in x:
    y.append(i**2)
mean = 0
counter = 0
for j in y:
    # print(j)
    mean += j
    counter += 1
# print(range(len(y)))
print(counter)
median = 0
if counter % 2 == 0:
    median = int(counter/2)
    median = y[median]
    print(median)
if counter % 2 == 1:
    x1 = counter // 2
    x2 = (counter // 2) + 1
    median = (y[x1] + y[x2]) / 2
    print(median)


# plt.plot(x, y)
# plt.plot([-2, 2, 3, 4], [1, 4, 9, 21]) #.plot ([x-coordinates], [y-coordinates])
# plt.axis([0, 2, -1, 10]) # .axis([x starting point, x ending point, y starting point, y ending point])
# plt.xlabel(), plt.ylabel()   #Labeling X and Y axis
# plt.plot([-2, 2, 3, 4], [1, 4, 9, 21], color='green', marker='x', linestyle='dashed', linewidth=2, markersize=12) # (x-coordinates, y-coordinates, line-color, how each plot is marked)
# plt.legend() #  Shows legend in graph
# plt.title() #  Adds a title to the top of the graph


# plt.show()