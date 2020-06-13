import tkinter as tk
import modules.series as s
import modules.vector as v

CANVAS_WIDTH = 700
CANVAS_HEIGHT = 700
SCALE = 50
SPEED = 0.1
guidelines = True

root = tk.Tk()
canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()

origin = CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2
millis_per_frame = int(1000 / 30)
time_in_millis = 0

label = tk.Label(root, text="Time: " + str(time_in_millis))
label.pack()

vectors = [v.VectorArrow(1 * SPEED, 1, 0)]
series = s.SeriesView(vectors, origin, canvas, SCALE)


def update_time():
    global time_in_millis, label, guidelines
    time_in_millis = time_in_millis + millis_per_frame
    label.configure(text="Time: " + str(time_in_millis / 1000))

    series.update_series(time_in_millis, guidelines)
    series.draw(time_in_millis)

    root.after(millis_per_frame, update_time)


def change_guidelines():
    global guidelines
    if guidelines:
        guidelines = False
        button['text'] = 'Add Guidelines'
    else:
        guidelines = True
        button['text'] = 'Remove Guidelines'


button = tk.Button(root, text='Remove Guidelines', command=change_guidelines)
button.pack()

update_time()

root.mainloop()
