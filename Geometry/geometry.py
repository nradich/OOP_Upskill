class Point:
    """Example class to work through fundamentals/ Holds point inputs"""
    def __init__(self, x:int, y:int):
        self.x =x
        self.y =y

    def fall_in_rectangle(self, lowleft:list, upright:list) -> bool:
        """Takes an input and compares vs the original instance """
        if lowleft[0] < self.x < upright[0]\
        and lowleft[1] < self.y < upright[1]:
            return True
        else:
            return False
        
    def distance_from_point(self, x ,y )-> int:
        """Determines the distance between x and y coordinates"""
        distance = ((self.x -x)**2 + (self.y - y)**2) **0.5
        return distance




class House :
    
    def __init__(self, wall_area ):
        self.wall_area = wall_area 

class Paint:

    def __init__(self, buckets: int, color: str) -> None:
        self.buckets = buckets
        self.color = color

Point1 = Point(10,20)

print(Point1.fall_in_rectangle([10,12], [15,23]))

print(Point(3,4).fall_in_rectangle([1,1], [6,6]))

print(Point(3,4).distance_from_point(5,6))

first_color = Paint(3, "blue")

print(first_color.buckets)