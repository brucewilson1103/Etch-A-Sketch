from turtle import Turtle, Screen

leo = Turtle()
screen = Screen()


def move_forward():
    leo.forward(10)

def move_back():
    leo.back(10)

def move_left():
    leo.left(10)

def move_right():
    leo.right(10)

def clear():
    leo.clear()
    leo.penup()
    leo.home()
    leo.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
