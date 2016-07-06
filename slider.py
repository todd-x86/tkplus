from control import Control
from Tkinter import Scale as TkScale

HORIZONTAL = 'horizontal'
VERTICAL = 'vertical'

class Slider(Control):
    def __init__(self, parent, **kwargs):
        Control.__init__(self, TkScale(parent._frame), **kwargs)
        self.min = 0
        self.max = 100
        self.value = 0
        self.ticks = 0
        self.show_label = False
        self.orientation = HORIZONTAL

    @property
    def min(self):
        return self._control_get('from')

    @min.setter
    def min(self, value):
        self._control_set('from', value)

    @property
    def max(self):
        return self._control_get('to')

    @max.setter
    def max(self, value):
        self._control_set('to', value)

    @property
    def value(self):
        return self._ctrl.get()

    @value.setter
    def value(self, value):
        self._ctrl.set(value)

    @property
    def ticks(self):
        return self._control_get('tickinterval')

    @ticks.setter
    def ticks(self, value):
        self._control_set('tickinterval', value)

    @property
    def orientation(self):
        return self._control_get('orient')

    @orientation.setter
    def orientation(self, value):
        self._control_set('orient', value)

    @property
    def show_label(self):
        return self._control_get('showvalue') == 1

    @show_label.setter
    def show_label(self, value):
        self._control_set('showvalue', 1 if value else 0)
