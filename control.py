from Tkinter import Frame as TkFrame, Canvas as TkCanvas
from collections import namedtuple

Rect = namedtuple('Rect', ['left', 'top', 'width', 'height'])

# Events for binding
EVENT_MOUSECLICK_RIGHT = '<Button-3>'

class BaseControl(object):
    def __init__(self, ctrl=None):
        self._ctrl = ctrl

    def bind(self, evt, callback):
        self._ctrl.bind(evt, callback)

    def _control_get(self, key):
        return self._ctrl.config().get(key)

    def _control_set(self, key, value):
        set_args = {key: value}
        self._ctrl.config(**set_args)

# Alignment types
ALIGN_BOTTOM = {'side':'bottom', 'fill':'x'}
ALIGN_TOP = {'side':'top', 'fill':'x'}
ALIGN_LEFT = {'side':'left', 'fill':'y'}
ALIGN_RIGHT = {'side':'right', 'fill':'y'}
ALIGN_CLIENT = {'fill':'both', 'expand':'1'}
ALIGN_NONE = None

class Control(BaseControl):
    def __init__(self, ctrl=None, **kwargs):
        BaseControl.__init__(self, ctrl)
        self._visible = False
        if ctrl:
            self._place(kwargs)
        self._popup = None
        self._align = ALIGN_NONE

    def _place(self, kwargs):
        self.left = kwargs['left']
        self.top = kwargs['top']
        self.width = kwargs['width']
        self.height = kwargs['height']
        self._visible = True

    @property
    def align(self):
        return self._align

    @align.setter
    def align(self, value):
        self._align = value
        self._reposition()

    @property
    def enabled(self):
        return self._enabled()

    def _enabled(self):
        self.update()
        return self._control_get('state') != 'disabled'

    @enabled.setter
    def enabled(self, value):
        if self._enabled() == value:
            return
        elif value:
            self._control_set('normal')
        else:
            self._control_set('disabled')

    @property
    def width(self):
        self.update()
        return self._ctrl.winfo_width()

    @width.setter
    def width(self, value):
        self.place(x=self.left, y=self.top, width=value, height=self.height)
        self.update()

    @property
    def left(self):
        self.update()
        return self._ctrl.winfo_x()

    @left.setter
    def left(self, value):
        self.place(x=value, y=self.top, width=self.width, height=self.height)
        self.update()

    @property
    def top(self):
        self.update()
        return self._ctrl.winfo_y()

    @top.setter
    def top(self, value):
        self.place(x=self.left, y=value, width=self.width, height=self.height)
        self.update()

    @property
    def height(self):
        self.update()
        return self._ctrl.winfo_height()

    @height.setter
    def height(self, value):
        self.place(x=self.left, y=self.top, width=self.width, height=value)
        self.update()

    @property
    def popup_menu(self):
        return self._popup

    @popup_menu.setter
    def popup_menu(self, value):
        self._popup = value
        if not value:
            self.bind(EVENT_MOUSECLICK_RIGHT, lambda x: "break")
        else:
            self.bind(EVENT_MOUSECLICK_RIGHT, self._invoke_popup)

    def _invoke_popup(self, event):
        self._popup.popup(event.x_root, event.y_root)
        return 'break'

    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, value):
        if self._visible == value:
            return
        elif value:
            self.show()
        else:
            self.hide()
        self._visible = value

    def on_show(self):
        pass

    def hide(self):
        if self._align == ALIGN_NONE:
            self._ctrl.place_forget()
        else:
            self._ctrl.pack_forget()

    def show(self):
        self.on_show()
        self._reposition()
        self.update()

    def _reposition(self):
        if self._align == ALIGN_NONE:
            # Place control
            self.place(x=self.left, y=self.top, width=self.width, height=self.height)
        else:
            # Pack / align control
            self.pack(**self._align)

    def refresh(self):
        self.update()

    def pack(self, *args, **kwargs):
        return self._ctrl.pack(*args, **kwargs)

    def place(self, *args, **kwargs):
        return self._ctrl.place(*args, **kwargs)

    def update(self):
        self._ctrl.update_idletasks()

# Text Control descendent

ALIGNMENT_LEFT = ('left', 'w')
ALIGNMENT_RIGHT = ('right', 'e')
ALIGNMENT_CENTER = ('center', 'center')

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
        return (self._control_get('justify'), self._control_get('anchor'))

    @alignment.setter
    def alignment(self, value):
        self._control_set('justify', value[0])
        self._control_set('anchor', value[1])

class CustomControl(Control):
    def __init__(self, parent, **kwargs):
        # NOTE: CustomControl is essentially the same as Panel except
        #       that Panel can be enhanced whereas CustomControl is
        #       to remain fairly minimal.
        Control.__init__(self, TkFrame(parent._frame), **kwargs)
        self._control_set('relief', 'flat')
        self._control_set('borderwidth', 0)
        self._frame = self._ctrl

class GraphicControl(Control):
    def __init__(self, parent, **kwargs):
        Control.__init__(self, TkCanvas(parent._frame), **kwargs)
        self._canvas = Canvas(self._ctrl)
        self._frame = self._ctrl
        self.repaint()

    @property
    def canvas(self):
        return self._canvas

    def refresh(self):
        self.clear()
        self.repaint()

    def clear(self):
        self._ctrl.delete('all')

    def repaint(self):
        self.on_paint()

    def on_paint(self):
        # NOTE: virtual method
        pass
