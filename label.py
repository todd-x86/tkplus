from control import TextControl, ALIGNMENT_LEFT
from Tkinter import Label as TkLabel

class Label(TextControl):
    def __init__(self, parent, **kwargs):
        TextControl.__init__(self, TkLabel(parent._frame), **kwargs)
        self.alignment = ALIGNMENT_LEFT
        self.wordwrap = False

    @property
    def caption(self):
        return self._control_get('text')

    @caption.setter
    def caption(self, value):
        self._control_set('text', value)

    @property
    def wordwrap(self):
        return self._control_get('wraplength') != 0

    @wordwrap.setter
    def wordwrap(self, value):
        self._control_set('wraplength', 0 if not value else self.width)
