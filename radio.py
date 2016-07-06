from control import TextControl, ALIGNMENT_LEFT
from Tkinter import Radiobutton as TkRadio, IntVar

STYLE_BUTTON = 0
STYLE_RADIO = 1

class RadioGroup(object):
    def __init__(self):
        self.var = IntVar()

class RadioButton(TextControl):
    def __init__(self, parent, **kwargs):
        TextControl.__init__(self, TkRadio(parent._frame), **kwargs)
        self.group = kwargs.get('group', RadioGroup())
        self.alignment = ALIGNMENT_LEFT

    @property
    def style(self):
        return self._control_get('indicatoron')

    @style.setter
    def style(self, value):
        self._control_set('indicatoron', value)

    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, value):
        self._group = value
        self._control_set('variable', value.var)

    @property
    def value(self):
        return self._control_get('value')[-1]

    @value.setter
    def value(self, value):
        self._control_set('value', value)

    @property
    def checked(self):
        return self.group.var.get() == self.value

    @checked.setter
    def checked(self, value):
        if value:
            self._ctrl.select()
        else:
            self._ctrl.deselect()
