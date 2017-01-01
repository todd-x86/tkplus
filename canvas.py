class Pen(object):
    def __init__(self):
        self.width = 1
        self.color = None

class Brush(object):
    def __init__(self):
        self.color = None

class CustomCanvas(object):
    def __init__(self):
        self._pen = Pen()
        self._brush = Brush()

    def line(self, x1, y1, x2, y2):
        pass

    def arc(self, x1, y1, x2, y2, angle1, angle2):
        pass

    def image(self, x1, y1, x2, y2):
        pass

    @property
    def pen(self):
        return self._pen

    @property
    def brush(self):
        return self._brush

class Canvas(CustomCanvas):
    def __init__(self, handle):
        CustomCanvas.__init__(self)
        self._handle = handle

    def line(self, x1, y1, x2, y2):
        line_args = {'width':self.pen.width, 'fill':self.pen.color}

        self._handle.create_line(x1, y1, x2, y2, **line_args)

    def arc(self, x1, y1, x2, y2, angle1, angle2):
        arc_args = {'width':self.pen.width,
                    'outline':self.pen.color,
                    'fill':self.brush.color,
                    'start':90-angle2,
                    'extent':angle2-angle1}

        self._handle.create_arc(x1, y1, x2, y2, **arc_args)

    def image(self, x1, y1, image):
        if isinstance(image, str):
            kwargs = {'file': image}
        else:
            kwargs = {'data': image}

        self._handle.create_image(x1, y1, **kwargs)

