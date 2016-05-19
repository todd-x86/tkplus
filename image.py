from control import Control
from Tkinter import PhotoImage, Label

class Picture(object):
    def __init__(self, tk_hnd):
        self._img = None
        self._hnd = tk_hnd

    def open_file(self, filename):
        self._img = PhotoImage(file=filename)        
        self.refresh()

    def refresh(self):
        if not self._img:
            return
        self._hnd.configure(image=self._img)

    def get_width(self):
        if not self._img:
            return None
        else:
            return self._img.width()

    def get_height(self):
        if not self._img:
            return None
        else:
            return self._img.height()

    width = property(get_width)
    height = property(get_height)

class Image(Control):
    def __init__(self, parent, left, top, width, height, data):
        super(self.__class__, self).__init__()
        self._ctrl = Label(master=parent._frame)
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self._picture = Picture(self._ctrl)
        self._picture.open_file(data)

    def get_picture(self):
        return self._picture

    picture = property(get_picture)
