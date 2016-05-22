from collections import namedtuple

Rect = namedtuple('Rect', ['left', 'top', 'width', 'height'])

class Control(object):
    def __init__(self):
        self._ctrl = None

    def _control_get(self, key):
        return self._ctrl.config().get(key)

    def _control_set(self, key, value):
        set_args = {key: value}
        self._ctrl.config(**set_args)

    @property
    def width(self):
        return self._ctrl.winfo_width()

    @width.setter
    def width(self, value):
        self._ctrl.place(x=self.left, y=self.top, width=value, height=self.height)
        self._ctrl.update_idletasks()

    @property
    def left(self):
        return self._ctrl.winfo_x()

    @left.setter
    def left(self, value):
        self._ctrl.place(x=value, y=self.top, width=self.width, height=self.height)
        self._ctrl.update_idletasks()

    @property
    def top(self):
        return self._ctrl.winfo_y()

    @top.setter
    def top(self, value):
        self._ctrl.place(x=self.left, y=value, width=self.width, height=self.height)
        self._ctrl.update_idletasks()

    @property
    def height(self):
        return self._ctrl.winfo_height()

    @height.setter
    def height(self, value):
        self._ctrl.place(x=self.left, y=self.top, width=self.width, height=value)
        self._ctrl.update_idletasks()
