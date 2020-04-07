import tkinter as tk
import math
from modules.vector import Vector, VectorArrow

CANVAS_WIDTH = 700
CANVAS_HEIGHT = 700
SCALE = 50

root = tk.Tk()
canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()

center = CANVAS_WIDTH/2, CANVAS_HEIGHT/2
millis_per_frame = int(1000 / 30)
time_in_millis = 0

label = tk.Label(root, text="Time: " + str(time_in_millis))
label.pack()

vectors = [VectorArrow(0.1, 0.1, 0, center, canvas, SCALE), VectorArrow(0.2, 2, 0, center, canvas, SCALE)]

def update_time():
    global time_in_millis, label
    time_in_millis = time_in_millis + millis_per_frame
    label.configure(text="Time: " + str(time_in_millis / 1000))

    for v in vectors:
        v.update_vector(time_in_millis)

    root.after(millis_per_frame, update_time)

update_time()

root.mainloop()