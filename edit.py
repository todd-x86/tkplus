from Tkinter import Entry, StringVar
from control import Control

class Edit(Control):
    def __init__(self, parent, left, top, width, height):
        super(self.__class__, self).__init__()
        self._text = StringVar()
        self._ctrl = Entry(master=parent._frame, textvariable=self._text)
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    @property
    def text(self):
        return self._text.get()

    @text.setter
    def text(self, value):
        self._text.set(value)
