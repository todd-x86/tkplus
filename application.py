import Tkinter

class Application(object):
    def __init__(self):
        self._running = False
        self._tk = Tkinter.Tk()
        self._icon = None

    def run(self, main_form, start_x=None, start_y=None):
        self._running = True
        if isinstance(main_form, list):
            for frm in main_form:
                self.run(frm, start_x, start_y)
        else:
            if not start_x:
                main_form.left = start_x
            if not start_y:
                main_form.top = start_y
            main_form.show()

    @property
    def running(self):
        return self._running

    @property
    def icon(self):
        return self._icon

    @icon.setter
    def set_icon(self, value):
        self._icon = value
        self._tk.wm_iconbitmap(value)

    def non_use(self):
        if not self._running:
            self._tk.withdraw()

app = Application()
