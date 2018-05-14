class Rectangle:
    def __init__(self, xcoor, ycoor, h, w):
        """
        Iniitializes class
        :param xcoor: x coordinate of upper left pos
        :param ycoor: y coordinate of upper left pos
        :param h: height
        :param w: width
        """
        self.x = xcoor
        self.y = ycoor
        self.height = h
        self.width = w

    def __str__(self):
        """
        Returns a string containing the objects attributes
        :return: rest_str
        """
        rect_str = "("+str(self.x)+","+str(self.y)+") width: "+str(self.width)+" height: "+str(self.height)
        return rect_str
