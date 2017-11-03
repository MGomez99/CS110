class Rectangle:
    def __init__(self, xcoor, ycoor, h, w):
        self.x = xcoor
        self.y = ycoor
        self.height = h
        self.width = w

    def __str__(self):
        rect_str = "("+str(self.x)+","+str(self.y)+") width: "+str(self.width)+" height: "+str(self.height)
        return rect_str
