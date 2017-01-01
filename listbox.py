from control import Control
from containers import ScrollContainer
from Tkinter import Listbox as TkListBox, END, BOTH, LEFT, RIGHT, Y

class ListItems(object):
    def __init__(self, control):
        self._list = control

    def __getitem__(self, index):
        return self.get(index)

    def get(self, index):
        return self._list._ctrl.get(index)

    def add(self, item):
        self.append(item)

    def append(self, item):
        self._list._ctrl.insert(END, item)

    def insert(self, index, item):
        self._list._ctrl.insert(index, item)

    def delete(self, index):
        self._list._ctrl.delete(index)

    def remove(self, item):
        index = self.index(item)
        if index >= 0:
            self.delete(index)

    def clear(self):
        self._list._ctrl.delete(0, END)

    def index(self, item):
        for index, tmp in enumerate(self._list._ctrl.get(0, END)):
            if item == tmp:
                return index
        return -1

    @property
    def count(self):
        return self._list._ctrl.size()

    @property
    def selected_count(self):
        return len(self._list._ctrl.curselection())

    @property
    def selected_keys(self):
        return map(int, self._list._ctrl.curselection())

    @selected_keys.setter
    def selected_keys(self, value):
        self._list._ctrl.select_clear(0, END)
        if value is not None:
            for index in value:
                self._list._ctrl.select_set(index)

    @property
    def selected_values(self):
        return map(self.get, self.selected_keys)

    @selected_values.setter
    def selected_values(self, value):
        self.selected_keys = filter(lambda x: x >= 0, map(self.index, value))

    def selected(self, index):
        return self._list._ctrl.selection_includes(index)

    def select(self, index):
        self._list._ctrl.select_set(index)

    def unselect(self, index):
        self._list._ctrl.select_clear(index)

class BaseListBox(Control):
    def __init__(self, parent, **kwargs):
        Control.__init__(self, TkListBox(parent._frame), **kwargs)
        self._items = ListItems(self)

    @property
    def items(self):
        return self._items

    @property
    def multiple(self):
        return self._control_get('selectmode') in ['extended', 'multiple']

    @multiple.setter
    def multiple(self, value):
        self._control_set('selectmode', 'extended' if value else 'browse')

    @property
    def checkboxes(self):
        return self._control_get('selectmode') == 'multiple'

    @checkboxes.setter
    def checkboxes(self, value):
        if self.multiple and not value:
            self._control_set('selectmode', 'extended')
        elif not value:
            self._control_set('selectmode', 'browse')
        else:
            self._control_set('selectmode', 'multiple')

class ListBox(ScrollContainer):
    def __init__(self, parent, **kwargs):
        ScrollContainer.__init__(self, parent, **kwargs)
        self._init_container(BaseListBox(self, **kwargs))
        
    # NOTE: ListBox by design implements a faceplate for ListBoxContainer properties
    @property
    def items(self):
        return self._container.items

    @property
    def multiple(self):
        return self._container.multiple

    @multiple.setter
    def multiple(self, value):
        self._container.multiple = value

    @property
    def checkboxes(self):
        return self._container.checkboxes

    @checkboxes.setter
    def checkboxes(self, value):
        self._container.checkboxes = value

    @property
    def popup_menu(self):
        return self._container.popup_menu

    @popup_menu.setter
    def popup_menu(self, value):
        self._container.popup_menu = value
