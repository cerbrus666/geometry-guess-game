class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, lowleft, upright):
        if lowleft[0] < self.x < upright[0] \
                and lowleft[1] < self.y < upright[1]:
            return True
        else:
            return False

    def distance(self, otherpoint):
        distancex = otherpoint.x - self.x
        distancey = otherpoint.y - self.y
        return ((distancex)**2  + (distancey)**2) ** 0.5




def main():
    point2 = Point(3, 4)
    print(point2.falls_in_rectangle((5, 6), (7, 9)))
    point3 = Point(7,8)
    print(point2.distance(point3))

main()
