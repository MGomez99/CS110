import Rectangle


class Surface:
    def __init__(self, filename, x, y, h, w):
        """
        Initializes surface
        :param filename:
        :param x: x coord for rectangle
        :param y: y coord for rectangle
        :param h: height of rectangle
        :param w: width of rectangle
        """
        self.image = filename
        self.rect = Rectangle.Rectangle(x, y, h, w)

    def getRect(self):
        """
        Gets the rectangles attributes
        :return: self.rect
        """
        return self.rect
