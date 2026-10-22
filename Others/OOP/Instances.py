class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_area(self):
        return self.height*self.width

Rec1 = Rectangle(2, 3)

print(Rec1.height)
print(Rectangle.get_area(Rec1))
