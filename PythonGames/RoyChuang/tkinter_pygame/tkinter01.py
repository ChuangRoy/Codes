from tkinter import *
from tkinter import colorchooser
tk = Tk()
c = colorchooser.askcolor()
print(c)


def create__button():
    def click():
        print("click")

    button = Button(tk, text="Click Me", command=click)
    button.pack()


def create_canvas():
    global canvas
    canvas = Canvas(tk, width=500, height=500)
    canvas.pack()


def draw_line(x1, y1, x2, y2):
    canvas.create_line(x1, y1, x2, y2)


def draw_rectangle(x1, y1, x2, y2, fill_color):
    canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)


def draw_rectangles():
    draw_rectangle(10, 10, 50, 50, "green")
    draw_rectangle(100, 100, 390, 140, "blue")
    draw_rectangle(200, 200, 240, 490, "red")


def draw_random_rectangles_100():
    import random
    for x in range(100):
        x1 = random.randrange(450)
        y1 = random.randrange(450)
        x2 = x1 + random.randrange(450)
        y2 = y1 + random.randrange(450)
        draw_rectangle(x1, y1, x2, y2, None)


def draw_arc(x1, y1, x2, y2, input_extent):
    canvas.create_arc(x1, y1, x2, y2, extent=input_extent, style=ARC)


def draw_different_arc():
    draw_arc(10, 10, 200, 80, 45)
    draw_arc(10, 80, 200, 160, 90)
    draw_arc(10, 160, 200, 240, 135)
    draw_arc(10, 240, 200, 320, 180)
    draw_arc(10, 320, 200, 400, 359)


def draw_triangle(x1, y1, x2, y2, x3, y3, input_fill):
    canvas.create_polygon(x1, y1, x2, y2, x3, y3,
                          fill=input_fill, outline="black")


def draw_polygons():
    draw_triangle(10, 10, 100, 10, 100, 110, "")
    canvas.create_polygon(200, 10, 240, 30, 120, 100, 140,
                          120, fill="", outline="black")


create_canvas()
# create__button()
# draw_line(0, 0, 500, 500)
# draw_rectangles()
# draw_random_rectangles_100()
# draw_arc(10, 10, 200, 100, 180)
# draw_different_arc()
draw_triangle(10, 10, 100, 10, 100, 110, "")
draw_polygons()

tk.mainloop()
