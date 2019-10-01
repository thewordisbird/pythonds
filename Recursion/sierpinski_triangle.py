import turtle

def sierpinski(l, t):
    if l > 50:
        t.forward(l)
        t.left(120)
        t.forward(l)
        t.left(120)
        t.forward(l)
        t.left(120)
        sierpinski(l/2, t)
        t.forward(l/2)
        sierpinski(l/2, t)
        t.backward(l/2)
        #t.left(60)
        t.forward(l/2)
        sierpinski(l/2, t)


if __name__ == '__main__':
    # Turtle setup
    t = turtle.Turtle()
    myWin = turtle.Screen()
   
    length = 600
    t.up()
    t.goto(-length/2, -length/2)
    t.down()
    sierpinski(length,t) 
    myWin.exitonclick()