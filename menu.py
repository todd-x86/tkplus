from control import BaseControl
from Tkinter import Menu as TkMenu

class MenuItem(object):
    def __init__(self, menu, title, **kwargs):
        self._menu = menu
        # NOTE: For whatever reason, lambdas do not work in this case...
        self._menu._ctrl.add_command(label=title, command=self._on_click)
        if kwargs.get('on_click'):
            self.on_click = kwargs['on_click']

    def _on_click(self):
        """Handler for keeping on_click virtual"""
        self.on_click()

    def on_click(self):
        pass

class BaseMenu(BaseControl):
    def __init__(self, parent_hnd, **kwargs):
        BaseControl.__init__(self, TkMenu(parent_hnd))
        if kwargs.get('tearoff'):
            self.tearoff = kwargs['tearoff']
        else:
            self.tearoff = False

    @property
    def tearoff(self):
        return self._control_get('tearoff') == 1

    @tearoff.setter
    def tearoff(self, value):
        self._control_set('tearoff', 1 if value else 0)

    def create(self, title, **kwargs):
        return MenuItem(self, title, **kwargs)

    def separator(self):
        self._ctrl.add_separator()

class Menu(BaseMenu):
    def __init__(self, menubar, title, **kwargs):
        BaseMenu.__init__(self, menubar._ctrl, **kwargs)
        self._mainmenu = menubar
        menubar._ctrl.add_cascade(label=title, menu=self._ctrl)

class MainMenu(BaseControl):
    def __init__(self, parent):
        BaseControl.__init__(self, TkMenu(parent._frame))
        parent._control_set('menu', self._ctrl)
        
    def create(self, title, **kwargs):
        return Menu(self, title, **kwargs)

class PopupMenu(BaseMenu):
    def __init__(self, parent, **kwargs):
        BaseMenu.__init__(self, parent._frame, **kwargs)

    def popup(self, x, y):
        try:
            self._ctrl.tk_popup(x, y, 0)
        finally:
            self._ctrl.grab_release()
