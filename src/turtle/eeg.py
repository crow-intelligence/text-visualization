import random
import turtle
from tkinter import *

s = turtle.getscreen()
t = turtle.Turtle()
t.speed(0)
t.shape("circle")
t.shapesize(0.1)


screen = turtle.Screen()
TURTLE_SIZE = 20

# t.penup()
# t.goto(TURTLE_SIZE/2 - screen.window_width()/2, screen.window_height()/2 - TURTLE_SIZE/2)
# t.pendown()


# morse
def generate_random_line():
    return [random.randint(0, 2) for i in range(80)]


def long():
    t.pendown()
    t.pen(pensize=3, pencolor="black")
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()


def short():
    # t.pen(pensize=3, pencolor="white")
    t.penup()
    t.forward(10)
    t.pendown()
    t.dot(10, "black")
    # t.pen(pensize=3, pencolor="white")
    t.penup()
    t.forward(10)
    t.pendown()


def space():
    t.penup()
    # t.pen(pensize=3, pencolor="white")
    t.forward(20)
    t.pendown()


novel = [generate_random_line() for i in range(100)]

i = TURTLE_SIZE / 2
for sequence in novel:
    t.penup()
    t.goto(TURTLE_SIZE / 2 - screen.window_width() / 2, screen.window_height() / 2 - i)
    t.pendown()
    for syllab in sequence:
        if syllab == 0:
            long()
        elif syllab == 1:
            short()
        else:
            space()
    i += 20

s.getcanvas().postscript(file="imgs/dots.eps")
