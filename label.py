from control import TextControl, ALIGNMENT_LEFT
from Tkinter import Label as TkLabel

class Label(TextControl):
    def __init__(self, parent, **kwargs):
        super(self.__class__, self).__init__()
        self._ctrl = TkLabel(parent._frame)
        self.caption = kwargs.get('caption')
        self.left = kwargs['left']
        self.top = kwargs['top']
        self.width = kwargs['width']
        self.height = kwargs['height']
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
