import math
import cmath


class Vector:

    def __init__(self, freq, magnitude, angle):
        self.freq = freq
        self.magnitude = magnitude
        self.angle = angle

    def __str__(self):
        return "n: " + str(self.freq) + \
               " | " + "magnitude: " + str(self.magnitude) + \
               " | " + "angle: " + str(self.angle)

    def get_value(self, time_in_millis):
        time_in_secs = time_in_millis / 1000
        return (self.magnitude * cmath.exp(self.angle * 1j)) * (cmath.exp(2 * math.pi * 1j * self.freq * time_in_secs))

    def get_freq(self):
        return self.freq

    def get_magnitude(self):
        return self.magnitude

    def get_angle(self):
        return self.angle


class VectorArrow(Vector):
    base_xy = []

    def __init__(self, freq, magnitude, angle):
        super().__init__(freq, magnitude, angle)
        self.polygon = None
        self.center = None

    def __str__(self):
        return super().__str__()

    @staticmethod
    def create_base_xy(scale):
        VectorArrow.base_xy = [(0, -0.02 * scale), (0, 0.02 * scale), (0.9 * scale, 0.02 * scale),
                               (0.9 * scale, 0.04 * scale), (scale, 0), (0.9 * scale, -0.04 * scale),
                               (0.9 * scale, -0.02 * scale)]

    def create_vector(self, canvas):
        self.polygon = canvas.create_polygon(VectorArrow.base_xy)
        # self.plot(canvas, center, scale)

    def update_vector(self, time_in_millis, center, canvas):
        new_xy = []
        self.center = center

        for x, y in VectorArrow.base_xy:
            angle = super().get_value(time_in_millis) * complex(x, y) + center
            new_xy.append(angle.real)
            new_xy.append(angle.imag)

        canvas.coords(self.polygon, new_xy)

    def plot(self, canvas, center, scale):
        radius = super().get_magnitude() * scale

        canvas.create_oval(center.real - radius, center.imag - radius, center.real + radius, center.imag + radius)

    def get_tip(self, time_in_millis, scale):
        return super().get_value(time_in_millis) * scale + self.center
