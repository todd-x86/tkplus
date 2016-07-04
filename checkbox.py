from control import TextControl, ALIGNMENT_LEFT
from Tkinter import Checkbutton as TkCheckbox, BooleanVar

class CheckBox(TextControl):
    def __init__(self, parent, **kwargs):
        super(self.__class__, self).__init__()
        self._ctrl = TkCheckbox(parent._frame)
        self._checkvar = BooleanVar()
        self._control_set('onvalue', True)
        self._control_set('offvalue', False)
        self._control_set('variable', self._checkvar)
        self.caption = kwargs.get('caption')
        self.left = kwargs['left']
        self.top = kwargs['top']
        self.width = kwargs['width']
        self.height = kwargs['height']
        self.alignment = ALIGNMENT_LEFT

    @property
    def checked(self):
        return self._checkvar.get()

    @checked.setter
    def checked(self, value):
        if value:
            self._ctrl.select()
        else:
            self._ctrl.deselect()
