import colorgram
import turtle as t

artist = t.Turtle()
screen = t.Screen()
t.colormode(255)

colors = colorgram.extract('hirstimg.jpg', 30)

rgb = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb.append(new_color)


i = 0
no_of_dots = 10
width = 20
gap = 50
jump = 0
artist.hideturtle()
for row in range(no_of_dots):
    artist.penup()
    artist.setheading(225)
    artist.forward(300)
    artist.setheading(0)
    artist.pendown()

    for column in range(no_of_dots):
        artist.pencolor(rgb[i])
        artist.dot(width)
        artist.penup()
        artist.forward(gap)
        artist.pendown()
        if i == len(colors) - 1:
            i = -1
        i += 1

    jump += gap
    artist.penup()
    artist.goto(0, jump)
    artist.pendown()

t.done()
