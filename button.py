from control import Control
from image import Picture
from Tkinter import Button as TkButton, PhotoImage

class Button(Control):
    def __init__(self, parent, **kwargs):
        Control.__init__(self, TkButton(parent._frame), **kwargs)
        self.caption = kwargs.get('caption')
        # NOTE: This lets 'command' behave like a virtual method
        self._control_set('command', lambda: self.on_click())
        
    def on_click(self):
        pass

    @property
    def caption(self):
        return self._control_get('text')

    @caption.setter
    def caption(self, value):
        self._control_set('text', value)

    def flash(self):
        self._ctrl.flash()

    @property
    def background(self):
        return self._control_get('background')

    @background.setter
    def background(self, value):
        self._control_set('background', value)
        self._control_set('activebackground', value)

    @property
    def default(self):
        return self._control_get('default') == 'active'

    @default.setter
    def default(self, value):
        self._control_set('default', 'active' if value else 'normal')

class BitBtn(Button):
    def __init__(self, parent, **kwargs):
        Button.__init__(self, parent, **kwargs)
        self._control_set('compound', 'left')
        self._glyph = Picture(self._ctrl)
        if kwargs.get('image'):
            self.glyph.open_file(kwargs['image'])

    @property
    def glyph(self):
        return self._glyph
