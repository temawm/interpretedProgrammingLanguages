import math

class Shape:
    def __init__(self, identifier, x, y):
        self.identifier = identifier
        self.x = x
        self.y = y

    def area(self):
        raise NotImplementedError("Подклассы доложны реализовывать этот метод.")


class Triangle(Shape):
    def __init__(self, identifier, x, y, base, height):
        super().__init__(identifier, x, y)
        self.base = base
        self.height = height

    def area(self):
        area = 0.5 * self.base * self.height
        if (area >= 0):
            return area
        else:
            print("Параметр меньше 0")
            return


class Pentagon(Shape):
    def __init__(self, identifier, x, y, side):
        super().__init__(identifier, x, y)
        self.side = side

    def area(self):
        area = (5 * self.side ** 2) / (4 * math.tan(math.pi / 5))
        if(area >= 0):
            return (5 * self.side ** 2) / (4 * math.tan(math.pi / 5))
        else:
            print("Параметр меньше 0")
            return


def compare(t1, t2):
    if not isinstance(t1, Shape) or not isinstance(t2, Shape):
        raise ShapeError("Оба объекта должны быть экземплярами Shape.")

    area1 = t1.area()
    area2 = t2.area()

    print(f"Сравнение площадей: {area1} и {area2}")
    if area1 > area2 :
        return area1 - area2
    else :
        return area2 - area1

def is_intersect(t1, t2):
    distance = math.sqrt((t1.x - t2.x) ** 2 + (t1.y - t2.y) ** 2)
    radius1 = math.sqrt(t1.area() / math.pi)
    radius2 = math.sqrt(t2.area() / math.pi)

    print(f"Дистанция между фигурами: {distance}")
    print(f"Радиус треугольника: {radius1}, Радиус пятиугольника: {radius2}")
    return distance < (radius1 + radius2)

try:
    triangle = Triangle("Triangle1", 0, 0, 10, 5)
    pentagon = Pentagon("Pentagon1", 4, 3, 6)

    print("Результат сравнения:", compare(triangle, pentagon))
    print("Пересечение", is_intersect(triangle, pentagon))

except Exception as e:
    print("Error:", e)
