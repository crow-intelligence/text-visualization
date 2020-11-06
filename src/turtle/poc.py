import turtle

import pandas as pd

df = pd.read_csv("data/processed/linevizdata.tsv",
                 sep="\t",
                 encoding="utf-8")

cluster_color = {
    0: (179, 88, 88),
    1: (206, 64, 183),
    2: (105, 95, 103),
    3: (125, 46,154),
    4: (82, 46, 154),
    5: (17, 24, 219),
    6: (59, 155, 179),
    7: (32, 223, 185),
    8: (10, 159, 20),
    9: (212, 164, 52)
}


s = turtle.getscreen()
s.screensize(s.window_width(), s.window_height())
print((s.window_width(), s.window_height()))

t = turtle.Turtle()
t.shape("circle")
t.shapesize(0.1)
t.hideturtle()
turtle.colormode(255)
t.penup()
t.right(90)
t.forward((s.window_height()/2))
t.left(90)
t.pendown()

for index, row in df.iterrows():
    print(index)
    color = cluster_color[row["cluster"]]
    t.pen(pensize=row["pagerank"]*3.2, pencolor=color)
    t.forward(row["length"]/15)
    t.right(90)

s.getcanvas().postscript(file="imgs/lines.eps")
