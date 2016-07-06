from control import Control
from Tkinter import Frame as TkFrame

BORDER_SINGLE = 'ridge'
BORDER_RAISED = 'raised'
BORDER_LOWERED = 'sunken'
BORDER_NONE = 'flat'

class Panel(Control):
    def __init__(self, parent, **kwargs):
        Control.__init__(self, TkFrame(parent._frame), **kwargs)
        self._frame = self._ctrl
        self.border_width = 1
        self.border_style = BORDER_SINGLE

    @property
    def border_width(self):
        return self._control_get('borderwidth')

    @border_width.setter
    def border_width(self, value):
        self._control_set('borderwidth', value)

    @property
    def border_style(self):
        return self._control_get('relief')

    @border_style.setter
    def border_style(self, value):
        self._control_set('relief', value)
