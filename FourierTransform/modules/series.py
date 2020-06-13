from modules.vector import Vector, VectorArrow


class Series:

    def __init__(self, vectors):
        self.vectors = vectors

    @classmethod
    def create_base_series(cls, terms):
        vectors = [Vector(0, 1, 0)]
        for i in range(0, terms // 2):
            vectors.insert(0, Vector(-i, 1, 0))
            vectors.append(Vector(i, 1, 0))

        return cls(vectors)

    def __str__(self):
        result = str(self.vectors[0])
        for v in self.vectors[1:]:
            result += "\n" + str(v)

        return result

    def get_value(self, time_in_millis):
        vector_sum = 0
        for v in self.vectors:
            vector_sum += v.get_value(time_in_millis)

        return vector_sum

    def get_vectors(self):
        return self.vectors


class SeriesView(Series):

    def __init__(self, vectors, origin, canvas, scale):
        super().__init__(vectors)
        self.origin = complex(origin[0], origin[1])
        self.canvas = canvas
        self.scale = scale
        VectorArrow.create_base_xy(scale)
        self.create_series()

    def __str__(self):
        return super().__str__()

    def create_series(self):
        for v in super().get_vectors():
            v.create_vector(self.canvas)

    def update_series(self, time_in_millis, guidelines):
        vectors = super().get_vectors()

        vectors[0].update_vector(time_in_millis, self.origin, self.canvas, self.scale, guidelines)

        for i in range(1, len(vectors)):
            tip = vectors[i-1].get_tip(time_in_millis, self.scale)
            vectors[i].update_vector(time_in_millis, tip, self.canvas, self.scale, guidelines)

    def draw(self, time_in_millis):
        radius = 1
        point = super().get_value(time_in_millis) * self.scale + self.origin

        self.canvas.create_oval(point.real - radius, point.imag - radius, point.real + radius, point.imag + radius)
