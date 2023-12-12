import turtle 
from random import randint


myturtle = turtle.Turtle()


myturtle.goto(50,75)
myturtle.forward(120) # go r
myturtle.left(90)
myturtle.forward(200)
myturtle.left(90)
myturtle.forward(120)
myturtle.left(90)
myturtle.forward(200)

turtle.done()

class Point:
    """Example class to work through fundamentals/ Holds point inputs"""
    def __init__(self, x:int, y:int):
        self.x =x
        self.y =y

    def fall_in_rectangle_point(self, lowleft:list, upright:list) -> bool:
        """Takes two points as  input and compares vs the original instance """
        if lowleft[0] < self.x < upright[0]\
        and lowleft[1] < self.y < upright[1]:
            return True
        else:
            return False
        
    def fall_in_rectangle(self, rectangle) -> bool:
        """Takes recetangle input and compares vs the original instance """
        if rectangle.point1.x < self.x \
        < rectangle.point2.x \
        and rectangle.point1.y < self.y < \
            rectangle.point2.y:
            return True
        else:
            return False
        
    def distance_from_point(self, x ,y )-> int:
        """Determines the distance between x and y coordinates"""
        distance = ((self.x -x)**2 + 
                 (self.y - y)**2) **0.5
        return distance

class Rectangle:

    def __init__(self, point1:str, point2:str ) -> None:
        """Take two points coordinates and store them as a rectangle """
        self.point1 = point1
        self.point2 = point2

    def area(self) -> float:
        """Calcualtes area of rectangle"""
        area = (self.point2.x - self.point1.x ) \
        * (self.point2.y - self.point1.y)

        return area
    
rectangle = Rectangle(Point(randint(0, 9), randint(0, 9)), 
              Point(randint(10, 19), randint(10, 19)))
 
# # Print rectangle coordinates
# print("Rectangle Coordinates: ",
#       rectangle.point1.x, ",",
#       rectangle.point1.y, "and",
#       rectangle.point2.x, ",",
#       rectangle.point2.y)
 
# # Get point and area from user
# user_point = Point(float(input("Guess x: ")), float(input("Guess y: ")))
# user_area = float(input("Guess rectangle area: "))
 
# # Print out the game result
# print("Your point was inside rectangle: ", user_point.fall_in_rectangle(rectangle))
# print("Your area was off by: ", rectangle.area() - user_area)
