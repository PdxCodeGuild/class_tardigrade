from turtle import*
r=0
while r < 18:
    h = 0
    while h <5:
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


    f = 0
    while f <5:
        pencolor("red")
        back(100)
        left(145)
        pencolor("green")
        back (100)
        left(145)
        pencolor("purple")
        back (100)
        left (145)
        pencolor("orange")
        back (100)
        left(145)
        f = f + 1
    g = 0
    while g <5:
        pencolor("red")
        back(100)
        right(145)
        pencolor("green")
        back (100)
        right(145)
        pencolor("purple")
        back (100)
        right (145)
        pencolor("orange")
        back (100)
        right(145)
        g = g + 1    
    r = r + 1
done()