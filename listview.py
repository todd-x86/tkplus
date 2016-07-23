from control import Control
from containers import ScrollContainer
from ttk import Treeview as TkTreeView

class ListViewColumn(object):
    def __init__(self, listview, caption, width):
        self._listview = listview
        self._caption = caption
        self._width = width
        self._index = -1

    @property
    def index(self):
        return self._index

    @property
    def caption(self):
        return self._caption

    @caption.setter
    def caption(self, value):
        self._caption = value
        key = '#{}'.format(self.index)
        self._listview._ctrl.heading(key, text=self._caption)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value
        key = '#{}'.format(self.index)
        self._listview._ctrl.column(key, width=self._width)

class ListViewColumns(object):
    def __init__(self, listview):
        self._listview = listview
        self._items = []

    def append(self, item):
        return self.add(item)

    @property
    def items(self):
        return map(lambda x: x[1], self._items)

    def add(self, item, width=100):
        col = ListViewColumn(self._listview, item, width)
        self._items.append(col)
        self.refresh()
        return col

    def insert(self, index, item, width=100):
        col = ListViewColumn(self._listview, item, width)
        self._items.insert(index, col)
        self.refresh()
        return col

    def delete(self, index):
        self._items.delete(index)
        self.refresh()

    def __getitem__(self, index):
        return self._items[index]

    @property
    def count(self):
        return len(self._items)

    def refresh(self):
        self._listview._control_set('columns', ['#{}'.format(j) for j in range(1, len(self._items))])
        for index, col in enumerate(self._items):
            col._index = index
            key = '#{}'.format(index)
            self._listview._ctrl.column(key, width=col.width)
            self._listview._ctrl.heading(key, text=col.caption)

class ListViewSubItems(object):
    def __init__(self, listview, iid):
        self._listview = listview
        self._iid = iid
        self._values = []

    def add(self, value):
        self._values.append(value)
        self.refresh()

    def __getitem__(self, index):
        return self._values[index]

    def __setitem__(self, index, value):
        self._values[index] = value
        self.refresh()

    @property
    def count(self):
        return len(self._values)

    def insert(self, index, value):
        self._values.insert(index, value)
        self.refresh()

    def delete(self, index):
        self._values.delete(index)
        self.refresh()

    def refresh(self):
        self._listview._ctrl.item(self._iid, values=self._values)

class ListViewItem(object):
    def __init__(self, listview, text, index='end'):
        self._listview = listview
        self._text = text
        self._index = -1
        self._iid = self._listview._ctrl.insert('', index, None, text=text)
        self._strings = ListViewSubItems(listview, self._iid)

    @property
    def index(self):
        return self._index

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
        self._listview._ctrl.item(self._iid, text=value)

    @property
    def subitems(self):
        return self._strings

    def delete(self):
        self._listview._ctrl.delete(self._iid)

class ListViewItems(object):
    def __init__(self, listview):
        self._listview = listview
        self._items = []

    def add(self, item):
        row = ListViewItem(self._listview, item)
        self._items.append(row)
        return row

    def __getitem__(self, index):
        return self._items[index]

    @property
    def count(self):
        return len(self._items)

    def delete(self, index):
        self._items[index].delete()
        self._items.delete(index)

    def insert(self, index, value):
        row = ListViewItem(self._listview, item)
        self._items.insert(index, row)
        return row

class BaseListView(Control):
    def __init__(self, parent, **kwargs):
        Control.__init__(self, TkTreeView(parent._frame), **kwargs)
        self._columns = ListViewColumns(self)
        self._items = ListViewItems(self)

    @property
    def columns(self):
        return self._columns

    @property
    def items(self):
        return self._items

class ListView(ScrollContainer):
    def __init__(self, parent, **kwargs):
        ScrollContainer.__init__(self, parent, **kwargs)
        self._init_container(BaseListView(self, **kwargs))
        # TODO: fix scrollbar issue with ListView

    @property
    def columns(self):
        return self._container.columns

    @property
    def items(self):
        return self._container.items

