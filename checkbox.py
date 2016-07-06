from control import TextControl, ALIGNMENT_LEFT
from Tkinter import Checkbutton as TkCheckbox, BooleanVar

class CheckBox(TextControl):
    def __init__(self, parent, **kwargs):
        TextControl.__init__(self, TkCheckbox(parent._frame), **kwargs)
        self._checkvar = BooleanVar()
        self._control_set('onvalue', True)
        self._control_set('offvalue', False)
        self._control_set('variable', self._checkvar)
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
