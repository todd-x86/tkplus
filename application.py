import Tkinter

class Application(object):
    def __init__(self):
        self._running = False

    def run(self, main_form, start_x=None, start_y=None):
        self._running = True
        if not start_x:
            main_form.left = start_x
        if not start_y:
            main_form.top = start_y
        main_form.show()

    @property
    def running(self):
        return self._running



app = Application()
