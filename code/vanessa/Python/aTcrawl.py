from turtle import*
color ()
i=0


fillcolor('blue')

n_sides = 8
edge_length = 0

i = 0

color("pink")
begin_fill()
pencolor("blue")
while i < 49:
	forward(edge_length)
	right(360/n_sides)
	i = i + 1
	edge_length = edge_length + 1
end_fill()

o = 0
while o < 50:
	forward (edge_length)
	left(360/n_sides)
	o = o + 1
	edge_length = edge_length + 1

h = 0
forward(180)
while h <25:
    pencolor("red")
    forward (100)
    left(145)
    pencolor("green")
    forward (100)
    left(145)
    pencolor("purple")
    forward (100)
    left(145)
    pencolor("orange")
    forward (100)
    left(145)
    h = h + 1
left(180)
pencolor("black")
forward (90)
left(90)
forward (90)
left(90)   
forward (90)
left(90)
forward (90)
left(90)
right(180)
right(180)
l = 0
while l <5:
    pencolor("red")
    forward (100)
    right(145)
    pencolor("green")
    forward (100)
    right(145)
    pencolor("purple")
    forward (100)
    right(145)
    pencolor("orange")
    forward (100)
    right(145)
    l = l + 1
pencolor("red")
fillcolor('black')
begin_fill()
left(180)
forward(100)
left(144)
forward(100)
left(144)
pencolor("orange")
forward(100)
left(144)
forward(100)
left(144)
pencolor("yellow")
forward (100)
left(144)
end_fill()
pencolor("black")
forward (45)
right(45)
forward (45)
right(45)   
forward (45)
right(45)
forward (45)
right(45)
forward (45)
right(45)
forward (45)
right(45)   
forward (45)
right(45)
forward (45)
right(45)
done ()