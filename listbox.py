from control import Control
from scrollbar import ScrollBar
from panel import Panel, BORDER_NONE
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

class ListBoxContainer(Control):
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

class ListBox(Panel):
    def __init__(self, parent, **kwargs):
        Panel.__init__(self, parent, **kwargs)
        container = ListBoxContainer(self, top=0, left=0, width=self.width, height=self.height)
        scrollbar = ScrollBar(self, top=0, left=self.width, height=self.height, width=28)
        self._yscroll = scrollbar
        # NOTE: This is just to hacky way to prevent the scrollbar from looking disabled
        self._yscroll.max = 1
        self._scrollbar_visible = False
        self._listbox = container
        self._bind()
        self.border_style = BORDER_NONE

    def _bind(self):
        # Pack listbox and eventually the scrollbar
        self._listbox._ctrl.pack(side=LEFT, fill=BOTH, expand=1)
        
        # Setup appropriate callbacks
        self._listbox._control_set('yscrollcommand', self._on_scroll_view)
        self._yscroll._control_set('command', self._on_scroll)

    def _show_scrollbar(self):
        self._yscroll._ctrl.pack(side=RIGHT, fill=Y)
        self._scrollbar_visible = True

    def _hide_scrollbar(self):
        self._yscroll._ctrl.tk.call('grid', 'remove', self._yscroll._ctrl)
        self._scrollbar_visible = False

    def _on_scroll_view(self, ymin, ymax):
        if self._scrollbar_visible and float(ymax)-float(ymin) == 1.0:
            self._show_scrollbar()
        elif not self._scrollbar_visible:
            self._show_scrollbar()
            
        self._yscroll._ctrl.set(ymin, ymax)

    def _on_scroll(self, *args):
        # Hacky way of chaining yview + on_scroll callback
        self._listbox._ctrl.yview(*args)
        # TODO: Make this an event handler
        self._yscroll.on_scroll(*args)

    # NOTE: ListBox by design implements a faceplate for ListBoxContainer properties
    @property
    def items(self):
        return self._listbox.items

    @property
    def multiple(self):
        return self._listbox.multiple

    @multiple.setter
    def multiple(self, value):
        self._listbox.multiple = value

    @property
    def checkboxes(self):
        return self._listbox.checkboxes

    @checkboxes.setter
    def checkboxes(self, value):
        self._listbox.checkboxes = value

    @property
    def popup_menu(self):
        return self._listbox.popup_menu

    @popup_menu.setter
    def popup_menu(self, value):
        self._listbox.popup_menu = value
        #self._ctrl.bind("<Button-3>", self._invoke_popup)
