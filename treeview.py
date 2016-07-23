from control import Control
from containers import ScrollContainer
from ttk import Treeview as TkTreeView

class TreeViewItem(object):
    def __init__(self, parent, treeview, text, **kwargs):
        self._treeview = treeview
        parent_ref = ''
        if parent:
            parent_ref = parent.reference
        self._ref = treeview._ctrl.insert(parent_ref, 'end', text=text, open=kwargs.get('open', False))
        self._text = text
        self._parent = parent
        self._items = TreeViewItems(treeview, self)

    @property
    def parent(self):
        return self._parent

    @property
    def reference(self):
        return self._ref

    def add(self, *args, **kwargs):
        return self._items.add(*args, **kwargs)

class TreeViewItems(object):
    def __init__(self, treeview, parent=None):
        self._treeview = treeview
        self._parent = parent
        self._items = []

    def __getitem__(self, index):
        return self._items[index]

    def add(self, *args, **kwargs):
        item = TreeViewItem(self._parent, self._treeview, *args, **kwargs)
        self._items.append(item)
        return item

class BaseTreeView(Control):
    def __init__(self, parent, **kwargs):
        Control.__init__(self, TkTreeView(parent._frame), **kwargs)
        self._items = TreeViewItems(self)
        self._ctrl['show'] = 'tree'

    @property
    def items(self):
        return self._items

class TreeView(ScrollContainer):
    def __init__(self, parent, **kwargs):
        ScrollContainer.__init__(self, parent, **kwargs)
        self._init_container(BaseTreeView(self, **kwargs))

    @property
    def items(self):
        return self._container.items

