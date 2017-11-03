import Rectangle


class Surface:
    def __init__(self, filename, x, y, h, w):
        self.image = filename
        self.rect = Rectangle.Rectangle(x, y, h, w)

    def getRect(self):
        return self.rect
