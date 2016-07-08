from control import Control
from ttk import Combobox as TkComboBox
from Tkinter import StringVar

class ComboItems(object):
    def __init__(self, combobox):
        self._combo = combobox
        self._values = []

    def _update_ctrl(self):
        self._combo._control_set('values', self._values)

    def __getitem__(self, index):
        return self.get(index)

    def get(self, index):
        return self._values[index]

    def add(self, item):
        self._values.append(item)
        self._update_ctrl()

    def append(self, item):
        self.add(item)

    def insert(self, index, item):
        self._values.insert(index, item)
        self._update_ctrl()

    def delete(self, index):
        self._values.pop(index)
        self._update_ctrl()

    def remove(self, item):
        index = self.index(item)
        if index >= 0:
            self.delete(index)

    def clear(self):
        self._values = []
        self._update_ctrl()

    def index(self, item):
        for index, tmp in enumerate(self._values):
            if item == tmp:
                return index
        return -1

    @property
    def count(self):
        return len(self._values)

    @property
    def selected(self):
        return self._combo._ctrl.current()

    @selected.setter
    def selected(self, index):
        self._combo._ctrl.current(index)

    @property
    def text(self):
        return self._combo.text

    @text.setter
    def text(self, value):
        self._combo.text = value

class ComboBox(Control):
    def __init__(self, parent, **kwargs):
        Control.__init__(self, TkComboBox(parent._frame), **kwargs)
        self._items = ComboItems(self)
        self._combotext = StringVar(self._ctrl)
        self._control_set('exportselection', 0)
        self._control_set('textvariable', self._combotext)

    @property
    def items(self):
        return self._items

    @property
    def text(self):
        return self._combotext.get()

    @text.setter
    def text(self, value):
        self._combotext.set(value)

    @property
    def readonly(self):
        return 'readonly' in self._control_get('state')

    @readonly.setter
    def readonly(self, value):
        if self.readonly == value:
            return
        elif value:
            self._control_set('state', 'readonly')
        else:
            self._control_set('state', 'normal')
