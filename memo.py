from control import Control
from containers import ScrollContainer
from Tkinter import Text, END

class _StringListWrapper(object):
    def __init__(self, ctrl):
        self._ctrl = ctrl

    @property
    def count(self):
        return int(self._ctrl.index('end').split('.')[0])

    def __getitem__(self, index):
        return self._get_line(index)

    def __setitem__(self, index, value):
        self._set_line(index, value)

    def _get_line(self, index):
        # TODO: check index
        # NOTE: Tkinter considers '1' the first line
        index = int(index)+1
        return self._ctrl.get("{}.0".format(index), "{}.end".format(index))

    def _set_line(self, index, value):
        # TODO: check index
        index = int(index)+1
        self._ctrl.delete("{}.0".format(index), "{}.end".format(index))
        self._ctrl.insert("{}.0".format(index), value)

    def clear(self):
        self._ctrl.delete("1.0", END)

    def open_file(self, filename):
        with open(filename, 'r') as fp:
            self.clear()
            for line in fp:
                self._ctrl.insert(END, line)

    def save_file(self, filename):
        with open(filename, 'w') as fp:
            fp.write(self._ctrl.get("1.0", END))


class BaseMemo(Control):
    def __init__(self, parent, **kwargs):
        Control.__init__(self, Text(master=parent._frame), **kwargs)
        self._line_wrapper = _StringListWrapper(self._ctrl)
        if kwargs.get('text'):
            self._ctrl.insert(END, kwargs['text'])

    @property
    def lines(self):
        return self._line_wrapper

    @property
    def text(self):
        return self._ctrl.get(1.0, END)

    @text.setter
    def text(self, value):
        self._ctrl.delete(1.0, END)
        self._ctrl.insert(END, str(value))

class Memo(ScrollContainer):
    def __init__(self, parent, **kwargs):
        ScrollContainer.__init__(self, parent, **kwargs)
        self._init_container(BaseMemo(self, **kwargs))

    @property
    def lines(self):
        return self._container.lines

    @property
    def text(self):
        return self._container.text

    @text.setter
    def text(self, value):
        self._container.text = value
