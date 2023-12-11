class Point:
    """Example class to work through fundamentals"""
    def __init__(self, x, y):
        self.x =x
        self.y =y

    def fall_in_rectangle(self, lowleft:int, upright:int):
        if lowleft < self.x < upright[0] \
        and lowleft[1] < self.y < upright[1]:
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

Point1 = Point(10,20)

print(Point1.x)

first_color = Paint(3, "blue")

print(first_color.buckets)