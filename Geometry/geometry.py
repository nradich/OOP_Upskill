class Point:
    """Example class to work through fundamentals/ Holds point inputs"""
    def __init__(self, x:int, y:int):
        self.x =x
        self.y =y

    def fall_in_rectangle(self, lowleft:int, upright:int):
        """Takes an input and compares vs the original instance """
        if lowleft < self.x < upright\
        and lowleft < self.y < upright:
            return True
        else:
            return False


class House :
    
    def __init__(self, wall_area ):
        self.wall_area = wall_area 

class Paint:

    def __init__(self, buckets: int, color: str) -> None:
        self.buckets = buckets
        self.color = color

Point1 = Point(10,11)

print(Point1.fall_in_rectangle(3,12))

first_color = Paint(3, "blue")

print(first_color.buckets)