import turtle
class Triangle:
    def __init__(self, start_point, length):
        self.length = length
        self.pts = [start_point, None, None]
    
    def get_start_point(self):
        return self.pts[0]
    
    def get_next_horiz_pt(self):
        return self.pts[1]

    def get_next_vert_pt(self):
        return self.pts[2]

    def get_length(self):
        return self.length

    def draw(self, t):
        t.up()
        t.goto(self.pts[0])
        t.setheading(0)
        
        # Draw Triangel
        t.down()
        for i in range(3):
            if self.pts[i] is None:
                self.pts[i] = t.pos()
            t.forward(self.length)
            t.left(120)
        
        t.up()

def sierpinski(t, tri):
    # Base case: Min length = 50
    if tri.get_length() >= 50:
        sierpinski(t,Triangle(tri.get_start_point(), tri.get_length()/2))
    else:
        tri.draw(t)
        sierpinski(t,Triangle(tri.get_next_horiz_pt(), tri.get_length()))
        # Move to Right and recures
        #t.goto(tri.get_next_horiz_pt())

        #t.goto(tri.get_start_point())
        #t.forward(tri.get_length())
        #input('pause')
        #sierpinski(t,Triangle(tri.get_next_horiz_pt(), tri.get_length()/2))
        
        # Move up and recures
        #t.goto(tri.get_start_point())
        #t.left(60)
        #t.forward(tri.get_length()/2)
        #sierpinski(t,Triangle(t.pos(), tri.get_length()/2))
        #tri.draw(t)
        #t.goto(tri.get_start_point())

if __name__ == '__main__':
    t = turtle.Turtle()
    myWin = turtle.Screen()
    #l = int(input('length: '))
    l = 400
    tri = Triangle((-l/2,-l/2), l)
    sierpinski(t, tri)

    myWin.exitonclick()