from control import Control
from Tkinter import Canvas as TkCanvas
from canvas import Canvas

class PaintBox(Control):
    def __init__(self, parent, **kwargs):
        Control.__init__(self, TkCanvas(parent._frame), **kwargs)
        self._canvas = Canvas(self._ctrl)

    @property
    def canvas(self):
        return self._canvas
