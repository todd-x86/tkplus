from control import Control
from image import Picture
from Tkinter import Button as TkButton, Spinbox as TkSpinBox, PhotoImage, END

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
        return self._raw_caption

    @caption.setter
    def caption(self, value):
        self._raw_caption = value
        amp_pos = -1

        # Sets the text and underline character (using '&' convention like in Windows)
        j = 0
        value_processed = ''
        while j < len(value):
            if value[j] == '&':
                j += 1
                if j < len(value) and value[j] != '&':
                    amp_pos = len(value_processed)
            value_processed += value[j]
            j += 1
        
        self._control_set('text', value_processed)
        self._control_set('underline', amp_pos)

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

class SpinButton(Control):
    def __init__(self, parent, **kwargs):
        Control.__init__(self, TkSpinBox(parent._frame), **kwargs)
        self.min = 0
        self.max = 100
        self.value = 0

    @property
    def min(self):
        return self._control_get('from')

    @min.setter
    def min(self, value):
        self._control_set('from', value)

    @property
    def max(self):
        return self._control_get('to')

    @max.setter
    def max(self, value):
        self._control_set('to', value)

    @property
    def value(self):
        return self._ctrl.get()

    @value.setter
    def value(self, value):
        self._ctrl.delete(0, END)
        self._ctrl.insert(END, value)

    @property
    def increment(self):
        return self._control_get('increment')

    @increment.setter
    def increment(self, value):
        return self._control_set('increment', value)

    @property
    def values(self):
        return self._control_get('values')

    @values.setter
    def values(self, value):
        return self._control_set('values', value)
