import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("cyan")

    brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("red")
    brad.speed(2)
    i=0
    while i < 4:
        brad.forward(200)
        brad.left(90)
        i += 1

    angie = turtle.Turtle()
    angie.color("blue")
    angie.circle(200)

    harry = turtle.Turtle()
    harry.color("purple")
    harry.shape("triangle")

    i = 0

    while i < 3:
        harry.forward(200)
        harry.right(120)
        i += 1

    window.exitonclick()

draw_shapes()