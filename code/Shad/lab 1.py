
import turtle
p = turtle.Screen()
p.bgcolor("purple")

y=turtle.Turtle()
y.shape('turtle')
y.color('orange')
l = y.clone()
l.color('green')

l.penup
y.pendown
l.write("I am" ,font=300)

while True:
    y.forward(100)
    y.left(90)
   

    l.forward(100)
    l.right(90)
  
