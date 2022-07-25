import turtle as t
import random

screen = t.Screen()
screen.colormode(255)
koopa = t.Turtle()
koopa.hideturtle()
color_list = [(207, 165, 127), (164, 169, 38), (140, 48, 106), (244, 79, 57), (3, 144, 60), (241, 66, 140),
              (249, 220, 224), (2, 142, 185), (162, 55, 52)]
koopa.penup()
koopa.setpos(-400, -350)
koopa.speed("fastest")
coordinates = 0

for xy in range(1, 14):
    coordinates += 50
    koopa.setpos(-400, -350 + coordinates)

    for dot in range(1, 17):
        koopa.dot(30, random.choice(color_list))
        koopa.forward(50)

screen.exitonclick()
