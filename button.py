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

    def flash(self):
        self._ctrl.flash()

    @property
    def background(self):
        return self._control_get('background')

    @background.setter
    def background(self, value):
        self._control_set('background', value)
        self._control_set('activebackground', value)

    @property
    def default(self):
        return self._control_get('default') == 'active'

    @default.setter
    def default(self, value):
        self._control_set('default', 'active' if value else 'normal')
