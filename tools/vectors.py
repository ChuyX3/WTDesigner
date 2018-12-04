class vector2(object):
    """description of class"""
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def add(self, other):
        self.x += other.x;
        self.y += other.y;

