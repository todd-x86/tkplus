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
        self._control_set('command', lambda: self.on_click())

    def on_click(self):
        pass

    @property
    def caption(self):
        return self._control_get('text')

    @caption.setter
    def caption(self, value):
        self._control_set('text', value)
