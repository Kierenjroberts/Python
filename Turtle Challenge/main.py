import random
import turtle as t

tim = t.Turtle()

t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


tim.shape("classic")
tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for x in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.left(360/36)


draw_spirograph(10)

screen = t.Screen()
screen.exitonclick()

direction = [0, 90, 180, 360]


