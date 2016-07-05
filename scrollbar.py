from control import Control
from Tkinter import Scrollbar as TkScrollbar

HORIZONTAL = 'horizontal'
VERTICAL = 'vertical'

class ScrollBar(Control):
    def __init__(self, parent, **kwargs):
        Control.__init__(self)
        self._ctrl = TkScrollbar(parent._frame)
        self.left = kwargs['left']
        self.top = kwargs['top']
        self.width = kwargs['width']
        self.height = kwargs['height']
        self._ctrl.set(0, 1)
        self._control_set('command', lambda *args: self._scroll(*args))
        self._min = 0
        self._max = 0
        self._value = 0
        self._window = 1

    def _scroll(self, *args):
        action = args[0]
        if action == 'moveto':
            delta = float(args[1])
            self.value = int(delta*float(self.max+self.window))
        elif action == 'scroll':
            delta = int(args[1])
            if self.min <= self.value+delta <= self.max:
                self.value += delta

    def on_scroll(self, value, delta):
        pass
    
    @property
    def orientation(self):
        return self._control_get('orient')

    @orientation.setter
    def orientation(self, value):
        self._control_set('orient', value)

    @property
    def min(self):
        return self._min

    @min.setter
    def min(self, value):
        self._min = value
        if value > self.value:
            self.value = value
        self._recalc()

    @property
    def max(self):
        return self._max

    @max.setter
    def max(self, value):
        self._max = value
        if value < self.value:
            self.value = value
        self._recalc()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        old = self._value
        self._value = value
        self._recalc()
        self.on_scroll(value, value-old)

    @property
    def window(self):
        return self._window

    @window.setter
    def window(self, value):
        self._window = value
        self._recalc()
        
    def _recalc(self):
        top = self.value/float(self.max+self.window)
        bottom = (self.value+self.window)/float(self.max+self.window)
        self._ctrl.set(top, bottom)
