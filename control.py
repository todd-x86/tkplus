from collections import namedtuple

Rect = namedtuple('Rect', ['left', 'top', 'width', 'height'])

class BaseControl(object):
    def __init__(self):
        self._ctrl = None

    def _control_get(self, key):
        return self._ctrl.config().get(key)

    def _control_set(self, key, value):
        set_args = {key: value}
        self._ctrl.config(**set_args)

class Control(BaseControl):
    def __init__(self):
        BaseControl.__init__(self)
        self._popup = None

    @property
    def width(self):
        return self._ctrl.winfo_width()

    @width.setter
    def width(self, value):
        self._ctrl.place(x=self.left, y=self.top, width=value, height=self.height)
        self._ctrl.update_idletasks()

    @property
    def left(self):
        return self._ctrl.winfo_x()

    @left.setter
    def left(self, value):
        self._ctrl.place(x=value, y=self.top, width=self.width, height=self.height)
        self._ctrl.update_idletasks()

    @property
    def top(self):
        return self._ctrl.winfo_y()

    @top.setter
    def top(self, value):
        self._ctrl.place(x=self.left, y=value, width=self.width, height=self.height)
        self._ctrl.update_idletasks()

    @property
    def height(self):
        return self._ctrl.winfo_height()

    @height.setter
    def height(self, value):
        self._ctrl.place(x=self.left, y=self.top, width=self.width, height=value)
        self._ctrl.update_idletasks()

    @property
    def popup_menu(self):
        return self._popup

    @popup_menu.setter
    def popup_menu(self, value):
        self._popup = value
        self._ctrl.bind("<Button-3>", self._invoke_popup)

    def _invoke_popup(self, event):
        self._popup.popup(event.x_root, event.y_root)    

# Text Control descendent

ALIGNMENT_LEFT = 'w'
ALIGNMENT_RIGHT = 'e'
ALIGNMENT_CENTER = 'center'

class TextControl(Control):
    def __init__(self):
        Control.__init__(self)

    @property
    def caption(self):
        return self._control_get('text')

    @caption.setter
    def caption(self, value):
        self._control_set('text', value)

    @property
    def alignment(self):
        return self._control_get('anchor')

    @alignment.setter
    def alignment(self, value):
        self._control_set('anchor', value)
