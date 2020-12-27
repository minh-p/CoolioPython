import turtle

def configureJeff():
    jeff = turtle.Turtle()
    jeff.color("blue")
    jeff.pensize(5)
    jeff.shape("turtle")
    jeff.speed(20)

    return jeff

def drawCircle():
    jeff = configureJeff()

    for _ in range(360):
        jeff.right(1)
        jeff.forward(2)

drawCircle()

input("")