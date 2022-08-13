class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, Rectangle):
        if Rectangle.lowleft.x < self.x < Rectangle.upright.x \
                and Rectangle.lowleft.y < self.y < Rectangle.upright.y:
            return True
        else:
            return False

    def distance(self, otherpoint):
        distancex = otherpoint.x - self.x
        distancey = otherpoint.y - self.y
        return ((distancex)**2 + (distancey)**2) ** 0.5


class Rectangle:

    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright

    def area(self):
        return (self.upright.x - self.lowleft.x) * (self.upright.y - self.lowleft.y)


def main():
    point2 = Point(3, 4)
    point3 = Point(7, 8)
    print(point2.distance(point3))

    point4 = Point(5, 6)
    rectangle_obj = Rectangle(Point(3, 4), Point(7, 8))
    print(point4.falls_in_rectangle(rectangle_obj))
    print("The area of rectangle object is:", rectangle_obj.area())


main()
