import tkinter as tk
from modules.Vector import Vector

root = tk.Tk()
canvas = tk.Canvas(width=200, height=200)
canvas.pack()

center = 100, 100
millis_per_frame = int(1000 / 30)
time = 0

label = tk.Label(root, text="Time: " + str(time))
label.pack()

xy = [(center[0], center[1] - 3), (center[0], center[1] + 3), (center[0] + 50, center[1] + 3), (center[0] + 50, center[1] + 6), (center[0] + 60, center[1]), (center[0] + 50, center[1] - 6), (center[0] + 50, center[1] - 3)]
polygon_item = canvas.create_polygon(xy)

def update_time():
    global time
    time = time + millis_per_frame
    offset = complex(center[0], center[1])
    new_xy = []

    v = Vector(0.1, complex(1, 0))

    for x, y in xy:
        angle = v.calc_angle(time) * (complex(x,y) - offset) + offset
        new_xy.append(angle.real)
        new_xy.append(angle.imag)

    canvas.coords(polygon_item, *new_xy)
    root.after(millis_per_frame, update_time)

update_time()

root.mainloop()