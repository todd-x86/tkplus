from Tkinter import Tk, Toplevel, Frame, BOTH
from control import Control, Rect
import os
import logging

log = logging.getLogger(__name__)

SINGLE = 0
TOOLWIN = 1

def check_handle(func):
    def call_with_check_handle(*args, **kwargs):
        Form._check_handle()
        return func(*args, **kwargs)

    return call_with_check_handle

class Form(Control):
    _main_form = None
    _active_forms = []

    @staticmethod
    def _check_handle():
        if not Form._main_form:
            tk = Tk()
            tk.withdraw()
    
    def __init__(self, **kwargs):
        Control.__init__(self)
        if not Form._main_form:
            Form._main_form = self
            master = Tk()
        else:
            master = Toplevel()
        master.withdraw()

        self._ctrl = master
        
        self._frame = Frame(master)
        self._frame.pack(fill=BOTH, expand=1)

        self._hidden_width = 0
        self._hidden_height = 0
        self.caption = kwargs.get('caption', 'Untitled')
        self.width = kwargs.get('width', 640)
        self.height = kwargs.get('height', 480)
        self._icon = None
        self._ctrl.protocol("WM_DELETE_WINDOW", self._on_close_handler)
        Form._active_forms.append(self)
        
    def on_close_query(self):
        return True

    def on_close(self):
        pass

    def _on_close_handler(self):
        if not self.on_close_query():
            return
        self.on_close()
        Form._active_forms.remove(self)
        self._ctrl.destroy()

    def _geometry(self):
        log.debug('_geometry -- {}'.format(self._ctrl.geometry()))
        if os.name != 'nt':
            self._ctrl.update_idletasks()
        (size, x, y) = self._ctrl.geometry().split('+')
        (width, height) = size.split('x')
        return Rect(*map(int, [x, y, width, height]))

    @property
    def width(self):
        if self.visible:
            return self._geometry().width
        else:
            return self._hidden_width

    @width.setter
    def width(self, value):
        self._hidden_width = value
        self._ctrl.geometry("{}x{}".format(value, self.height))
        self._ctrl.update_idletasks()

    @property
    def left(self):
        return self._geometry().left

    @left.setter
    def left(self, value):
        self._ctrl.geometry("+{}+{}".format(value, self.top))
        self._ctrl.update_idletasks()

    @property
    def top(self):
        return self._geometry().top

    @top.setter
    def top(self, value):
        self._ctrl.geometry("+{}+{}".format(self.left, value))
        self._ctrl.update_idletasks()

    @property
    def height(self):
        if self.visible:
            return self._geometry().height
        else:
            return self._hidden_height

    @height.setter
    def height(self, value):
        self._hidden_height = value
        self._ctrl.geometry("{}x{}".format(self.width, value))
        self._ctrl.update_idletasks()

    @property
    def caption(self):
        return self._ctrl.title()

    @caption.setter
    def caption(self, value):
        self._ctrl.title(value)

    @property
    def resizable(self):
        return self._ctrl.resizable() != '0 0'

    @resizable.setter
    def resizable(self, value):
        if not isinstance(value, bool):
            raise Exception('resizable value must be a bool')
        self._ctrl.resizable(int(value),int(value))
        self._ctrl.update_idletasks()

    @property
    def form_type(self):
        if os.name == 'nt':
            return int(self._ctrl.attributes('-toolwindow'))
        else:
            return SINGLE

    @form_type.setter
    def form_type(self, value):
        if os.name != 'nt':
            return
        if value not in [SINGLE, TOOLWIN]:
            raise Exception('Invalid form type')
        self._ctrl.attributes('-toolwindow', value)

    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
        self._ctrl.wm_iconbitmap(value)

    @property
    def visible(self):
        return self._ctrl.state() != 'withdrawn'

    @visible.setter
    def visible(self, value):
        if self.visible == value:
            return
        elif value:
            self.show()
        else:
            self.hide()
        
    def show(self):    
        self._ctrl.update()
        self._ctrl.deiconify()
        if self == Form._main_form:
            self._frame.mainloop()

    def hide(self):
        self._ctrl.withdraw()

    def close(self):
        self._on_close_handler()

    def show_modal(self):
        self.show()
        if self == Form._main_form:
            return
        self._ctrl.grab_set()
        for form in Form._active_forms:
            if form != self:
                form._ctrl.wait_window(self._ctrl)
