class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def set_x(self, value: int):
        self.x = value

    def set_y(self, value: int):
        self.y = value

    def __str__(self):
        return f"The point has coordinates ({self.x},{self.y})"



p = Point(2, 4)
print(p)
p.set_x(3)
p.set_y(5)
print(p)
