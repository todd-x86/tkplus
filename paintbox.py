from control import Control
from Tkinter import Canvas

class Pen(object):
    def __init__(self):
        self.width = 1
        self.color = None

class Brush(object):
    def __init__(self):
        self.color = None

class PaintBox(Control):
    def __init__(self, parent, left, top, width, height):
        super(self.__class__, self).__init__()
        self._ctrl = Canvas(parent._frame)
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self._pen = Pen()
        self._brush = Brush()

    def line(self, x1, y1, x2, y2):
        line_args = {'width':self.pen.width, 'fill':self.pen.color}
        self._ctrl.create_line(x1, y1, x2, y2, **line_args)

    def arc(self, x1, y1, x2, y2, angle1, angle2):
        arc_args = {'width':self.pen.width,
                    'outline':self.pen.color,
                    'fill':self.brush.color,
                    'start':90-angle2,
                    'extent':angle2-angle1}
        self._ctrl.create_arc(x1, y1, x2, y2, **arc_args)

    def image(self, x1, y1, image):
        if isinstance(image, str):
            kwargs = {'file': image}
        else:
            kwargs = {'data': image}
        self._ctrl.create_image(x1, y1, **kwargs)

    def get_pen(self):
        return self._pen

    def get_brush(self):
        return self._brush

    pen = property(get_pen)
    brush = property(get_brush)
