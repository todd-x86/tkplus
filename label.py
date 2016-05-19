from control import Control
from Tkinter import Label as TkLabel

class Label(Control):
    def __init__(self, parent, caption, left, top, width, height):
        super(self.__class__, self).__init__()
        self._ctrl = TkLabel(parent._frame)
        self.caption = caption
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def get_caption(self):
        return self._control_get('text')

    def set_caption(self, value):
        self._control_set('text', value)

    caption = property(get_caption, set_caption)
