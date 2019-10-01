import turtle
# draw a recursive tree using turtle
def draw_tree(branch_length, t):
    if branch_length < 15:
        return
    else:
        t.forward(branch_length)
        t.right(20)
        draw_tree(.75 * branch_length, t)
        t.left(40)
        draw_tree(.75 * branch_length, t)
        t.right(20)
        t.backward(branch_length)

if __name__ == '__main__':
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(150)
    t.down()
    draw_tree(75,t)
    t.left(60)
    draw_tree(75, t)
    t.left(60)
    draw_tree(75, t)
    t.left(60)
    draw_tree(75, t)
    t.left(60)
    draw_tree(75, t)
    t.left(60)
    draw_tree(75, t)
    t.left(30)
    draw_tree(50,t)
    t.left(60)
    draw_tree(50, t)
    t.left(60)
    draw_tree(50, t)
    t.left(60)
    draw_tree(50, t)
    t.left(60)
    draw_tree(50, t)
    t.left(60)
    draw_tree(50, t)


    myWin.exitonclick()