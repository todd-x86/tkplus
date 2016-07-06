from Tkinter import Entry, StringVar
from control import Control

class Edit(Control):
    def __init__(self, parent, **kwargs):
        Control.__init__(self, Entry(master=parent._frame), **kwargs)
        self._text = StringVar()
        self._control_set('textvariable', self._text)

    @property
    def text(self):
        return self._text.get()

    @text.setter
    def text(self, value):
        self._text.set(value)
