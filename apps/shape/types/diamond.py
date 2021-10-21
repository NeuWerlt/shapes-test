from apps.shape.types import ShapeTypeAbstract


class Diamond(ShapeTypeAbstract):
    parameters = ['diagonal_1', 'diagonal_2']

    def area(self):
        return self.diagonal_1 * self.diagonal_2

    def perimeter(self):
        return 2 * ((self.diagonal_1**2 + self.diagonal_2**2) ** 0.5)
