import math

class Vector:

    def __init__(self, freq, magn, angle):
        self.freq = freq
        self.magn = magn
        self.angle = angle

    def get_value(self, time_in_millis):
        time_in_secs = time_in_millis / 1000
        return (self.magn * math.e**(self.angle * 1j))*(math.e**(2 * math.pi * 1j * self.freq * time_in_secs))

    def get_freq(self):
        return self.freq

    def get_magn(self):
        return self.magn

    def get_angle(self):
        return self.angle

class VectorArrow(Vector):

    def __init__(self, freq, magn, angle, center, canvas, scale):
        super().__init__(freq, magn, angle)
        self.xy = VectorArrow.base_xy(scale)
        self.polygon = None
        self.center = complex(center[0], center[1])
        self.canvas = canvas
        self.scale = scale
        self.create_vector()

    @staticmethod
    def base_xy(scale):
        return [(0, -0.02 * scale), (0, 0.02 * scale), (0.9 * scale, 0.02 * scale), (0.9 * scale, 0.04 * scale), (scale, 0), (0.9 * scale, -0.04 * scale), (0.9 * scale, -0.02 * scale)]

    def create_vector(self):
        new_xy = []

        for x, y in self.xy:
            origin = complex(x,y) + self.center
            new_xy.append((origin.real, origin.imag))

        self.xy = new_xy
        self.polygon = self.canvas.create_polygon(self.xy)
        self.plot()

    def update_vector(self, time_in_millis):
        new_xy = []

        for x, y in self.xy:
            angle = super().get_value(time_in_millis) * (complex(x,y) - self.center) + self.center
            new_xy.append(angle.real)
            new_xy.append(angle.imag)

        self.canvas.coords(self.polygon, new_xy)

    def plot(self):
        radius = super().get_magn() * self.scale

        self.canvas.create_oval(self.center.real - radius, self.center.imag - radius, self.center.real + radius, self.center.imag + radius)

