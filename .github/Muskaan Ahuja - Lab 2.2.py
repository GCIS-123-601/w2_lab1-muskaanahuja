import turtle
def turtle_state():
    turtle.isdown()
    turtle.heading()
    turtle.xcor(), turtle.ycor()
def my_turtle():
    turtle.forward(100)
    turtle.left(87)
    turtle.setheading(127)
    turtle.up()
    turtle.goto(50,40)
    turtle.down()
    turtle.home()
    turtle.circle(25)
def main():
    turtle_state()
    my_turtle()
    turtle_state()
    input("press any key to continue..")
main()