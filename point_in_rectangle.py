from random import randint
import turtle


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


class GuiRectangle(Rectangle):

    def draw(self, canvas):

        # Go to a certain coordinates
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)

        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)  # Move 100 pixels
        canvas.left(90)  # Turn 90 degree left
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)



class GuiPoint(Point):

    def draw(self, canvas, size=5, color='red'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


def main():

    ############## Simple Point ###########################
    # point2 = Point(3, 4)
    # point3 = Point(7, 8)
    # print(point2.distance(point3))

    # point4 = Point(5, 6)
    # rectangle_obj = Rectangle(Point(3, 4), Point(7, 8))
    # print(point4.falls_in_rectangle(rectangle_obj))
    # print("The area of rectangle object is:", rectangle_obj.area())

    ############## Rectangle Game ########################
    # rectangle = Rectangle(Point(randint(0, 400), randint(
    #     0, 400)), Point(randint(0, 400), randint(0, 400)))

    # print("Rectangle coordinates: ", rectangle.point1.x, ",",
    #       rectangle.point1.y, ",", rectangle.point2.x, ",", rectangle.point2.y, ",")

    # # User inputs
    # user_point = Point(float(input("Guess x: ")), float(input("Guess y: ")))

    # # Print out result
    # print("Your point was inside rectangle: ",
    #       user_point.falls_in_rectangle(rectangle))

    ########### Basic GUI #########################
    # gui_rectangle = GuiRectangle(Point(randint(0, 400), randint(
    #     0, 400)), Point(randint(0, 400), randint(0, 400)))

    # myturtle = turtle.Turtle()

    # gui_rectangle.draw(canvas=myturtle)

    ########### Point GUI ##############################

    rectangle = GuiRectangle(Point(randint(0, 400), randint(
        0, 400)), Point(randint(0, 400), randint(0, 400)))

    print("Rectangle coordinates: ", rectangle.point1.x, ",",
          rectangle.point1.y, ",", rectangle.point2.x, ",", rectangle.point2.y, ",")

    # User inputs
    user_point = GuiPoint(float(input("Guess x: ")), float(input("Guess y: ")))

    # Print out result
    print("Your point was inside rectangle: ",
          user_point.falls_in_rectangle(rectangle))

    myturtle = turtle.Turtle()
    rectangle.draw(canvas=myturtle)
    user_point.draw(canvas=myturtle)
    turtle.done()


main()
