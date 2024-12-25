from geometric_figure import GeometricFigure
from color import Color

class Rectangle(GeometricFigure):
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = Color(color)

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height}, color={self.color.color}, area={self.area()})"
