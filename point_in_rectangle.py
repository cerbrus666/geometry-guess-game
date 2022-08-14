from random import randint


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, Rectangle):
        if Rectangle.point1.x < self.x < Rectangle.point2.x \
                and Rectangle.point1.y < self.y < Rectangle.point2.y:
            return True
        else:
            return False

    def distance(self, otherpoint):
        distancex = otherpoint.x - self.x
        distancey = otherpoint.y - self.y
        return ((distancex)**2 + (distancey)**2) ** 0.5


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)


def main():
    # point2 = Point(3, 4)
    # point3 = Point(7, 8)
    # print(point2.distance(point3))

    # point4 = Point(5, 6)
    # rectangle_obj = Rectangle(Point(3, 4), Point(7, 8))
    # print(point4.falls_in_rectangle(rectangle_obj))
    # print("The area of rectangle object is:", rectangle_obj.area())

    rectangle = Rectangle(Point(randint(0, 400), randint(
        0, 400)), Point(randint(0, 400), randint(0, 400)))

    print("Rectangle coordinates: ", rectangle.point1.x, ",",
          rectangle.point1.y, ",", rectangle.point2.x, ",", rectangle.point2.y, ",")

    # User inputs
    user_point = Point(float(input("Guess x: ")), float(input("Guess y: ")))

    # Print out result
    print("Your point was inside rectangle: ",
          user_point.falls_in_rectangle(rectangle))


main()
