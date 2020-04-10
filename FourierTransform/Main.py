import tkinter as tk
import math
from modules.vector import VectorArrow
from modules.series import SeriesView

CANVAS_WIDTH = 700
CANVAS_HEIGHT = 700
SCALE = 50
SPEED = 0.1

root = tk.Tk()
canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()

origin = CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2
millis_per_frame = int(1000 / 30)
time_in_millis = 0

label = tk.Label(root, text="Time: " + str(time_in_millis))
label.pack()

vectors = [VectorArrow(0 * SPEED, 0, 0),
           VectorArrow(1 * SPEED, 1.5, 0),
           VectorArrow(-1 * SPEED, 1, math.pi/2),
           VectorArrow(2 * SPEED, 0.5, math.pi),
           VectorArrow(-2 * SPEED, 1.3, 0),
           VectorArrow(3 * SPEED, 2, 1.7),
           VectorArrow(-3 * SPEED, 0.9, 1.37)]
series = SeriesView(vectors, origin, canvas, SCALE)


def update_time():
    global time_in_millis, label
    time_in_millis = time_in_millis + millis_per_frame
    label.configure(text="Time: " + str(time_in_millis / 1000))

    series.update_series(time_in_millis)
    series.draw(time_in_millis)

    root.after(millis_per_frame, update_time)


update_time()

root.mainloop()
