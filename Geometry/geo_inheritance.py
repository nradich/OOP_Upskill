import turtle 
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
        if rectangle.lowleft.x < self.x \
        < rectangle.upright.x \
        and rectangle.lowleft.y < self.y < \
            rectangle.upright.y:
            return True
        else:
            return False
        
    def distance_from_point(self, x ,y )-> int:
        """Determines the distance between x and y coordinates"""
        distance = ((self.x -x)**2 + 
                 (self.y - y)**2) **0.5
        return distance

class Rectangle:

    def __init__(self, lowleft:str, upright:str ) -> None:
        """Take two points coordinates and store them as a rectangle """
        self.lowleft = lowleft
        self.upright = upright

    def area(self) -> float:
        """Calcualtes area of rectangle"""
        area = (self.upright.x - self.lowleft.x ) \
        * (self.upright.y - self.lowleft.y)

        return area
