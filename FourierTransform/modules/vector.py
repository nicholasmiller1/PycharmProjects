import math
import tkinter as tk

class Vector:

    def __init__(self, freq, magn, angle):
        self.freq = freq
        self.magn = magn
        self.angle = angle

    def calc_angle(self, time_in_millis):
        time_in_secs = time_in_millis / 1000
        return (self.magn * math.e**(self.angle * 1j))*(math.e**(2 * math.pi * 1j * self.freq * time_in_secs))

    def get_freq(self):
        return self.freq

    def get_magn(self):
        return self.magn

    def get_angle(self):
        return self.angle

class VectorArrow(Vector):

    def __init__(self, freq, magn, angle):
        super().__init__(freq, magn, angle)
        self.xy = []
        self.polygon = None

    def create_vector(self, center, canvas):
        scale = super().get_magn()
        base = 5
        self.xy = [(center[0], center[1] - (base * scale)), (center[0], center[1] + (base * scale)), (center[0] + (10 * base * scale), center[1] + (base * scale)),
              (center[0] + (10 * base * scale), center[1] + (2 * base * scale)), (center[0] + (12 * base * scale), center[1]), (center[0] + (10 * base * scale), center[1] - (2 * base * scale)),
              (center[0] + (10 * base * scale), center[1] - (base * scale))]
        self.polygon = canvas.create_polygon(self.xy)

    def update_vector(self, time_in_millis, center, canvas):
        offset = complex(center[0], center[1])
        new_xy = []

        for x, y in self.xy:
            angle = super().calc_angle(time_in_millis) * (complex(x,y) - offset) + offset
            new_xy.append(angle.real)
            new_xy.append(angle.imag)

        canvas.coords(self.polygon, *new_xy)

