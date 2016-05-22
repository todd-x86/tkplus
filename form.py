from Tkinter import Tk, Toplevel, Frame, BOTH
from control import Control, Rect

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
    
    def __init__(self, caption="Untitled", width=600, height=400, parent=None):
        super(self.__class__, self).__init__()
        if not Form._main_form:
            Form._main_form = self
            master = Tk()
        else:
            master = Toplevel()
            master.withdraw()

        self._ctrl = master
        self._frame = Frame(master)
        self._frame.pack(fill=BOTH, expand=1)

        self.set_caption(caption)
        self.set_width(width)
        self.set_height(height)
        self._icon = None
        self._ctrl.protocol("WM_DELETE_WINDOW", self.on_close)
        self._add_to_active_list()

    def on_close(self):
        self._remove_from_active_list()
        self._ctrl.destroy()

    def _add_to_active_list(self):
        Form._active_forms.append(self)

    def _remove_from_active_list(self):
        Form._active_forms.remove(self)

    def _geometry(self):
        (size, x, y) = self._ctrl.geometry().split('+')
        (width, height) = size.split('x')
        return Rect(*map(int, [x, y, width, height]))

    def get_width(self):
        return self._geometry().width

    def set_width(self, value):
        self._ctrl.geometry("{}x{}".format(value, self.get_height()))
        self._ctrl.update_idletasks()

    def get_left(self):
        return self._geometry().left

    def set_left(self, value):
        self._ctrl.geometry("+{}+{}".format(value, self.get_top()))
        self._ctrl.update_idletasks()

    def get_top(self):
        return self._geometry().top

    def set_top(self, value):
        self._ctrl.geometry("+{}+{}".format(self.get_left(), value))
        self._ctrl.update_idletasks()

    def get_height(self):
        return self._geometry().height

    def set_height(self, value):
        self._ctrl.geometry("{}x{}".format(self.get_width(), value))
        self._ctrl.update_idletasks()

    def get_caption(self):
        return self._ctrl.title()

    def set_caption(self, value):
        self._ctrl.title(value)

    def get_resizable(self):
        return self._ctrl.resizable() != '0 0'

    def set_resizable(self, value):
        if not isinstance(value, bool):
            raise Exception('resizable value must be a bool')
        self._ctrl.resizable(int(value),int(value))
        self._ctrl.update_idletasks()

    def get_form_type(self):
        return int(self._ctrl.attributes('-toolwindow'))

    def set_form_type(self, value):
        if value not in [SINGLE, TOOLWIN]:
            raise Exception('Invalid form type')
        self._ctrl.attributes('-toolwindow', value)

    def get_icon(self):
        return self._icon

    def set_icon(self, value):
        self._icon = value
        self._ctrl.wm_iconbitmap(value)
        
    def show(self):
        if self == Form._main_form:
            self._frame.mainloop()
        else:
            self._ctrl.update()
            self._ctrl.deiconify()

    def hide(self):
        self._ctrl.withdraw()

    def show_modal(self):
        self.show()
        if self == Form._main_form:
            return
        self._ctrl.grab_set()
        for form in Form._active_forms:
            if form != self:
                form._ctrl.wait_window(self._ctrl)

    left = property(get_left, set_left)
    top = property(get_top, set_top)
    width = property(get_width, set_width)
    height = property(get_height, set_height)
    caption = property(get_caption, set_caption)
    resizable = property(get_resizable, set_resizable)
    form_type = property(get_form_type, set_form_type)
    icon = property(get_icon, set_icon)
