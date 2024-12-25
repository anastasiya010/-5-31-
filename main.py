from rectangle import Rectangle
from circle import Circle
from square import Square
import numpy as np

N = 5

rectangle = Rectangle(N, N, "blue")
circle = Circle(N, "green")
square = Square(N, "red")

print(rectangle)
print(circle)
print(square)

# Пример использования numpy
array = np.array([1, 2, 3])
print("Numpy array:", array)
