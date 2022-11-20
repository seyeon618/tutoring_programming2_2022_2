import math

class Circle:
    def __init__(self, radius, cx, cy):
        self.radius = radius
        self.x = cx
        self.y = cy

    def getArea(self):
        return self.radius * self.radius * math.pi

    def getCenter(self):
        return self.x, self.y

radius = int(input("반지름을 입력하시오: "))
x = int(input("x 좌표를 입력하시오: "))
y = int(input("y 좌표를 입력하시오: "))

circle = Circle(radius, x, y)
print("원의 넓이: ", circle.getArea())
print("원의 중심점: ", circle.getCenter())