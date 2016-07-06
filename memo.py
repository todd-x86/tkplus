from control import Control
from Tkinter import Text, END

class Memo(Control):
    def __init__(self, parent, **kwargs):
        Control.__init__(self, Text(master=parent._frame), **kwargs)
        if kwargs.get('text'):
            self._ctrl.insert(END, kwargs['text'])

    @property
    def text(self):
        return self._ctrl.get(1.0, END)

    @text.setter
    def text(self, value):
        self._ctrl.delete(1.0, END)
        self._ctrl.insert(END, value)
