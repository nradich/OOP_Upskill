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
        distance = ((self.x -x)**2 + 
                 (self.y - y)**2) **0.5
        return distance



class House :

    def __init__(self, wall_area ):
        self.wall_area = wall_area 

    def paint_needed(self) -> int:
        """Determines paint need for wall"""
        need = self.wall_area * 2.5
        return need 

class Paint:

    def __init__(self, buckets: int, color: str) -> None:
        self.buckets = buckets
        self.color = color

    def total_price(self) -> float:
        if self.color.lower() == "white":
            price = 1.99
        else:
            price = 2.19
        return price * self.buckets 

Point1 = Point(10,20)

print(Point1.fall_in_rectangle([10,12], [15,23]))
Point2 = Point(8,9)

print(Point(3,4).fall_in_rectangle([1,1], [6,6]))

print(Point(3,4).distance_from_point(Point2.x,Point2.y))

first_color = Paint(3, "white")

print(first_color.buckets)

print( House(4).paint_needed())
print ( first_color.total_price())