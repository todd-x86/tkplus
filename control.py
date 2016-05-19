from application import Application
from collections import namedtuple

Rect = namedtuple('Rect', ['left', 'top', 'width', 'height'])

class Control(object):
    def __init__(self):
        self._ctrl = None
        
    def _tk_ref(self, ref):
        if isinstance(ref, Application):
            return ref._tk
        else:
            return ref

    def _control_get(self, key):
        return self._ctrl.config().get(key)

    def _control_set(self, key, value):
        set_args = {key: value}
        self._ctrl.config(**set_args)

    def get_width(self):
        return self._ctrl.winfo_width()

    def set_width(self, value):
        self._ctrl.place(x=self.get_left(), y=self.get_top(), width=value, height=self.get_height())
        self._ctrl.update_idletasks()

    def get_left(self):
        return self._ctrl.winfo_x()

    def set_left(self, value):
        self._ctrl.place(x=value, y=self.get_top(), width=self.get_width(), height=self.get_height())
        self._ctrl.update_idletasks()

    def get_top(self):
        return self._ctrl.winfo_y()

    def set_top(self, value):
        self._ctrl.place(x=self.get_left(), y=value, width=self.get_width(), height=self.get_height())
        self._ctrl.update_idletasks()

    def get_height(self):
        return self._ctrl.winfo_height()

    def set_height(self, value):
        self._ctrl.place(x=self.get_left(), y=self.get_top(), width=self.get_width(), height=value)
        self._ctrl.update_idletasks()

    left = property(get_left, set_left)
    top = property(get_top, set_top)
    width = property(get_width, set_width)
    height = property(get_height, set_height)
