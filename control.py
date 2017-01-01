from Tkinter import Frame as TkFrame
from collections import namedtuple

Rect = namedtuple('Rect', ['left', 'top', 'width', 'height'])

class BaseControl(object):
    def __init__(self, ctrl=None):
        self._ctrl = ctrl

    def _control_get(self, key):
        return self._ctrl.config().get(key)

    def _control_set(self, key, value):
        set_args = {key: value}
        self._ctrl.config(**set_args)

class Control(BaseControl):
    def __init__(self, ctrl=None, **kwargs):
        BaseControl.__init__(self, ctrl)
        self._visible = False
        if ctrl:
            self._place(kwargs)
        self._popup = None

    def _place(self, kwargs):
        self.left = kwargs['left']
        self.top = kwargs['top']
        self.width = kwargs['width']
        self.height = kwargs['height']
        self._visible = True

    @property
    def enabled(self):
        self._ctrl.update_idletasks()
        return self._control_get('state') != 'disabled'

    @enabled.setter
    def enabled(self, value):
        if self.enabled == value:
            return
        elif value:
            self._control_set('normal')
        else:
            self._control_set('disabled')

    @property
    def width(self):
        self._ctrl.update_idletasks()
        return self._ctrl.winfo_width()

    @width.setter
    def width(self, value):
        self._ctrl.place(x=self.left, y=self.top, width=value, height=self.height)
        self._ctrl.update_idletasks()

    @property
    def left(self):
        self._ctrl.update_idletasks()
        return self._ctrl.winfo_x()

    @left.setter
    def left(self, value):
        self._ctrl.place(x=value, y=self.top, width=self.width, height=self.height)
        self._ctrl.update_idletasks()

    @property
    def top(self):
        self._ctrl.update_idletasks()
        return self._ctrl.winfo_y()

    @top.setter
    def top(self, value):
        self._ctrl.place(x=self.left, y=value, width=self.width, height=self.height)
        self._ctrl.update_idletasks()

    @property
    def height(self):
        self._ctrl.update_idletasks()
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
        if not value:
            self._ctrl.bind("<Button-3>", lambda x: "break")
        else:
            self._ctrl.bind("<Button-3>", self._invoke_popup)

    def _invoke_popup(self, event):
        self._popup.popup(event.x_root, event.y_root)
        return 'break'

    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, value):
        if self.visible == value:
            return
        elif value:
            self.show()
        else:
            self.hide()

    def on_show(self):
        pass

    def hide(self):
        self._ctrl.place_forget()

    def show(self):
        self.on_show()
        self._ctrl.place(x=self.left, y=self.top, width=self.width, height=self.height)
        self._ctrl.update_idletasks()

    def refresh(self):
        self._ctrl.update_idletasks()

# Text Control descendent

ALIGNMENT_LEFT = 'w'
ALIGNMENT_RIGHT = 'e'
ALIGNMENT_CENTER = 'center'

class TextControl(Control):
    def __init__(self, ctrl, **kwargs):
        Control.__init__(self, ctrl, **kwargs)
        self.caption = kwargs.get('caption')

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

class CustomControl(Control):
    def __init__(self, parent, **kwargs):
        # NOTE: CustomControl is essentially the same as Panel except
        #       that Panel can be enhanced whereas CustomControl is
        #       to remain fairly minimal.
        Control.__init__(self, TkFrame(parent._frame), **kwargs)
        self._control_set('relief', 'flat')
        self._control_set('borderwidth', 0)
        self._frame = self._ctrl
