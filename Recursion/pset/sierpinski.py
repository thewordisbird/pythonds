import turtle
class Triangle:
    def __init__(self, start_point, length):
        self.start_point = start_point
        self.length = length
    
    def get_start_point(self):
        return self.start_point

    def get_length(self):
        return self.length

    def draw(self, t):
        t.up()
        t.goto(self.start_point)
        t.setheading(0)
        end = t.pos()
        
        # Draw Triangel
        t.down()
        for i in range(3):
            t.forward(self.length)
            t.left(120)
        
        t.up()

def sierpinski(t, tri):
    # Base case: Min length = 50
    if tri.get_length() <= 50:
        tri.draw(t)
    else:
        #tri.draw(t)
        sierpinski(t,Triangle(tri.get_start_point(), tri.get_length()/2))
        tri.draw(t)
        # Move to Right and recures
        t.goto(tri.get_start_point())
        t.forward(tri.get_length()/2)
        sierpinski(t,Triangle(t.pos(), tri.get_length()/2))
        
        # Move up and recures
        t.goto(tri.get_start_point())
        t.left(60)
        t.forward(tri.get_length()/2)
        sierpinski(t,Triangle(t.pos(), tri.get_length()/2))

        t.goto(tri.get_start_point())

if __name__ == '__main__':
    t = turtle.Turtle()
    myWin = turtle.Screen()
    #l = int(input('length: '))
    l = 500
    tri = Triangle((-l/2,-l/2), l)
    sierpinski(t, tri)

    myWin.exitonclick()