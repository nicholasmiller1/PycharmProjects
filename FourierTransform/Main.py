import tkinter as tk
import math

canvas = tk.Canvas(width=200, height=200)
canvas.pack()

center = 100, 100

xy = [(center[0], center[1] - 3), (center[0], center[1] + 3), (center[0] + 50, center[1] + 3), (center[0] + 50, center[1] + 6), (center[0] + 60, center[1]), (center[0] + 50, center[1] - 6), (center[0] + 50, center[1] - 3)]
polygon_item = canvas.create_polygon(xy)

def getangle(event):
    dx = canvas.canvasx(event.x) - center[0]
    dy = canvas.canvasy(event.y) - center[1]
    try:
        return complex(dx, dy) / abs(complex(dx, dy))
    except ZeroDivisionError:
        return 0.0

def press(event):
    global start
    start = getangle(event)

def motion(event):
    global start
    angle = getangle(event) / start
    offset = complex(center[0], center[1])
    newxy = []

    for x, y in xy:
        v = angle * (complex(x,y) - offset) + offset
        newxy.append(v.real)
        newxy.append(v.imag)

    canvas.coords(polygon_item, *newxy)

canvas.bind("<Button-1>", press)
canvas.bind("<B1-Motion>", motion)

tk.mainloop()