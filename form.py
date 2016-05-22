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

        self.caption = caption
        self.width = width
        self.height = height
        self._icon = None
        self._ctrl.protocol("WM_DELETE_WINDOW", self._on_close_handler)
        self._add_to_active_list()

    def on_close_query(self):
        return True

    def on_close(self):
        pass

    def _on_close_handler(self):
        if not self.on_close_query():
            return
        self.on_close()
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

    @property
    def width(self):
        return self._geometry().width

    @width.setter
    def width(self, value):
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
        return self._geometry().height

    @height.setter
    def height(self, value):
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
        return int(self._ctrl.attributes('-toolwindow'))

    @form_type.setter
    def form_type(self, value):
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
