import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("cyan")

    brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("red")
    brad.speed(2)
    brad.forward(200)
    brad._rotate(90)
    brad.forward(200)
    brad._rotate(90)
    brad.forward(200)
    brad._rotate(90)
    brad.forward(200)
    brad._rotate(90)

    window.exitonclick()

draw_square()