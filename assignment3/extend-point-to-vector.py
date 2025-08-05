import math

class Point:
  def __init__(self, x: float, y: float):
    self.x = float(x)
    self.y = float(y)

  def __eq__(self, other):
    if not isinstance(other, Point):
      return NotImplemented
    return self.x == other.x and self.y == other.y

  def __str__(self):
    return f"Point({self.x}, {self.y})"

  def distance_euclidean(self, other):
    if not isinstance(other, Point):
      return NotImplemented
    return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

class Vector(Point):
  def __init__(self, x: float, y: float):
    super().__init__(x, y)

  def __str__(self):
    return f"Vector({self.x}, {self.y})"

  def __add__(self, other):
    if not isinstance(other, Vector):
      return NotImplemented
    return Vector(self.x + other.x, self.y + other.y)

# some tests
point1 = Point(1, 2)
point2 = Point(4, 6)
point3 = Point(1, 2)
vector1 = Vector(1, 2)
vector2 = Vector(3, 4)

print(point1)
print(str(point1))
print(point1 == point2)
print(point1 == point3)
print(point2 == "something else")
print(point1.distance_euclidean(point2))
print(vector1)
print(vector2)
print(vector1 + vector2)

