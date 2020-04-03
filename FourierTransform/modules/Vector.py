import math

class Vector:

    def __init__(self, freq, const):
        self.freq = freq
        self.const = const

    def calc_angle(self, time_in_millis):
        time_in_secs = time_in_millis / 1000
        return self.const*(math.e**(2 * math.pi * 1j * self.freq * time_in_secs))