

'''
Lab 1: Turtle
Author: Travis Jackson
Date: 11/16/21
'''

from turtle import *

i = 0
color_count = 1
speed(0)


while i < 200:

    forward( i * .1)
    left(5)
    i = i + 1

    # restart and set new color
    if i ==  200 :
        penup()
        setposition(0,0)
        i = 1
        pendown()

        #change color
        if color_count == 1:
            pencolor("green")
        elif color_count == 2:
            pencolor("red")
        elif color_count == 3:
            pencolor("blue")
        elif color_count == 4:
            pencolor("black")
        elif color_count == 5:
            break

        color_count = color_count + 1              

done()