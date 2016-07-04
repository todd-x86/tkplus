from control import Control
from Tkinter import Text, END

class Memo(Control):
    def __init__(self, parent, **kwargs):
        super(self.__class__, self).__init__()
        self._ctrl = Text(master=parent._frame)
        self.left = kwargs['left']
        self.top = kwargs['top']
        self.width = kwargs['width']
        self.height = kwargs['height']
        if kwargs.get('text'):
            self._ctrl.insert(END, kwargs['text'])

    @property
    def text(self):
        return self._ctrl.get(1.0, END)

    @text.setter
    def text(self, value):
        self._ctrl.delete(1.0, END)
        self._ctrl.insert(END, value)
