import turtle
def turtle_state():
    isDown=turtle.isdown()
    currAng=turtle.heading()
    xCord=turtle.xcor()
    yCord=turtle.ycor()
    return isDown,currAng,xCord,yCord
def test_drive():
    turtle.forward(100)
    turtle.left(87)
    turtle.setheading(127)
    turtle.up()
    turtle.goto(50,40)
    turtle.down()
    turtle.home()
    turtle.circle(25)
def main():
    stateBefore=turtle_state()
    print("Before Drawing")
    print("The Pen State is DOWN (T/F):"+str(stateBefore[0]))
    print("The Angle of Orientation is:"+str(stateBefore[1]))
    print("The X-Coordinate="+str(stateBefore[2])+" The Y-Coordinate="+str(stateBefore[3]))

    test_drive()

    stateAfter=turtle_state()
    print("After Drawing")
    print("The Pen State is DOWN (T/F):"+str(stateAfter[0]))
    print("The Angle of Orientation is:"+str(stateAfter[1]))
    print("The X-Coordinate="+str(stateAfter[2])+" The Y-Coordinate="+str(stateAfter[3]))

    input("press any key to continue..")
main()
