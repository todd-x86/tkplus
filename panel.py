from control import Control
from Tkinter import Frame as TkFrame

BORDER_SINGLE = 'ridge'
BORDER_RAISED = 'raised'
BORDER_LOWERED = 'sunken'
BORDER_NONE = 'flat'

class Panel(Control):
    def __init__(self, parent, **kwargs):
        super(self.__class__, self).__init__()
        self._ctrl = TkFrame(parent._frame)
        self._frame = self._ctrl
        self.left = kwargs['left']
        self.top = kwargs['top']
        self.width = kwargs['width']
        self.height = kwargs['height']
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
