import turtle

def tree(width, branch_len, t):
    if branch_len > 5:
        t.width(width)
        t.forward(branch_len)
        t.right(20)
        tree(width - 2, branch_len - 15, t)
        t.left(40)
        tree(width - 2, branch_len - 15, t)
        t.right(20)
        t.backward(branch_len)

if __name__ == "__main__":
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color('brown', 'green')
    tree(10, 75, t)
    myWin.exitonclick()