class Shape:
    def accept(self, visitor):
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor):
        visitor.visit_circle(self)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def accept(self, visitor):
        visitor.visit_rectangle(self)


class ShapeVisitor:
    def visit_circle(self, circle):
        raise NotImplementedError

    def visit_rectangle(self, rectangle):
        raise NotImplementedError


class AreaCalculator(ShapeVisitor):
    def visit_rectangle(self, rectangle):
        print(f"Площадь прямоугольника: {rectangle.width * rectangle.height}")

    def visit_circle(self, circle):
        print(f"Площадь круга: {3.14 * circle.radius ** 2}")


shapes = [
    Circle(5),
    Rectangle(4, 6)
]

visitor = AreaCalculator()

for shape in shapes:
    shape.accept(visitor)


# =============

class FigureDescriber(ShapeVisitor):
    def visit_rectangle(self, rectangle):
        print(f"Прямоугольник {rectangle.width}x{rectangle.height}")

    def visit_circle(self, circle):
        print(f"Круг с радиусом {circle.radius}")


shapes = [
    Circle(5),
    Rectangle(4, 6)
]

visitor = FigureDescriber()

for shape in shapes:
    shape.accept(visitor)
