from control import Control
from ttk import Progressbar as TkProgressBar

class ProgressBar(Control):
    def __init__(self, parent, **kwargs):
        Control.__init__(self, TkProgressBar(), **kwargs)

        self._min = 0
        self._max = 0
        self._value = 0
        
        self.max = 100
        self.min = 0
        self.value = 50

    @property
    def max(self):
        return self._max

    @max.setter
    def max(self, value):
        self._max = value
        self._recalc()

    @property
    def min(self):
        return self._min

    @min.setter
    def min(self, value):
        self._min = value
        self._recalc()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        self._recalc()

    def step(self, value):
        self.value += value

    def _recalc(self):
        self._control_set('maximum', self._max-self._min)
        self._control_set('value', self._value-self._min)
