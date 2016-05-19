from control import Control
from Tkinter import Button as TkButton

class Button(Control):
    def __init__(self, parent, caption, left, top, width, height):
        super(self.__class__, self).__init__()
        self._ctrl = TkButton(parent._frame)
        self.caption = caption
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def get_caption(self):
        return self._control_get('text')

    def set_caption(self, value):
        self._control_set('text', value)

    def get_on_click(self):
        return self._control_get('command')

    def set_on_click(self, callback):
        self._control_set('command', callback)

    caption = property(get_caption, set_caption)
    on_click = property(get_on_click, set_on_click)
